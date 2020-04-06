from datetime import timedelta
from datetime import datetime
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago

import pandas as pd

	
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': days_ago(2),
    'email': ['airflow@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=3),
    # 'queue': 'bash_queue',
    # 'pool': 'backfill',
    # 'priority_weight': 10,
    # 'end_date': datetime(2016, 1, 1),
    # 'wait_for_downstream': False,
    # 'dag': dag,
    # 'sla': timedelta(hours=2),
    # 'execution_timeout': timedelta(seconds=300),
    # 'on_failure_callback': some_function,
    # 'on_success_callback': some_other_function,
    # 'on_retry_callback': another_function,
    # 'sla_miss_callback': yet_another_function,
    # 'trigger_rule': 'all_success'
}

def prepararDatos():
    # Obtener columnas de fecha y temperatura
	temp_fp = "/tmp/temperature.csv"
	temp_file = open(temp_fp, newline='')
	temp_df = pd.read_csv(temp_file)
	temp_datetime = temp_df[['datetime','San Francisco']]

	# Obtener columnas de fecha y humedad
	hum_fp = "/tmp/humidity.csv"
	hum_file = open(hum_fp, newline='')
	hum_df = pd.read_csv(hum_file)
	hum_datetime = hum_df[['datetime','San Francisco']]

	# Cambiar el nombre de las columnas 
	temp_datetime = temp_datetime.rename(columns={"San Francisco": "temperature"})
	hum_datetime = hum_datetime.rename(columns={"San Francisco": "humidity"})

	# Unir dataframes 
	date_temp_hum_df = pd.merge(temp_datetime, hum_datetime, on='datetime')

	# Eliminar filas con valores vacíos
	df = date_temp_hum_df.dropna()

	# Guardar en un fichero
	df.to_csv ("/tmp/weather.csv", index = False, header=True)



#Inicialización del grafo DAG de tareas para el flujo de trabajo
dag = DAG(
    'practica2',
    default_args=default_args,
    description='Automatización del despliegue del servicio de prediccion',
    schedule_interval=timedelta(days=1),
)

# Operadores o tareas
DescargarDatosHumedad = BashOperator(
    task_id='descargar_datos_humedad',
    depends_on_past=False,
    bash_command='wget https://github.com/manuparra/MaterialCC2020/raw/master/humidity.csv.zip -O /tmp/humidity.csv.zip',
    dag=dag,
)

DescargarDatosTemperatura = BashOperator(
    task_id='descargar_datos_temperatura',
    depends_on_past=False,
    bash_command='wget https://github.com/manuparra/MaterialCC2020/raw/master/temperature.csv.zip -O /tmp/temperature.csv.zip',
    dag=dag,
)

DescomprimirDatos = BashOperator(
    task_id='descomprimir_datos',
    depends_on_past=True,
    bash_command='unzip -d /tmp -o /tmp/humidity.csv.zip & unzip -d /tmp -o /tmp/temperature.csv.zip',
    dag=dag,
)

PrepararDatos = PythonOperator(
    task_id='preparar_datos',
    depends_on_past=True,
    python_callable=prepararDatos,
    dag=dag,
)

DescargarFuenteGithub = BashOperator(
    task_id='descargar_fuente_github',
    depends_on_past=False,
    bash_command='wget https://github.com/toniMR/CloudComputing-Servicios_y_Aplicaciones/archive/master.zip -O /tmp/CloudComputing-Servicios_y_Aplicaciones.zip && unzip -d /tmp -o /tmp/CloudComputing-Servicios_y_Aplicaciones.zip',
    dag=dag,
)

DesplegarContenedorMongo = BashOperator(
    task_id='desplegar_contenedor_mongo',
    depends_on_past=True,
    bash_command='cd /tmp/CloudComputing-Servicios_y_Aplicaciones-master/practica2/docker && docker-compose up -d db',
    dag=dag,
)

InsertarDatosMongo = BashOperator(
    task_id='insertar_datos_mongo',
    depends_on_past=True,
    bash_command='mongoimport -d cc-db -c weather --type csv --file /tmp/weather.csv --headerline',
    dag=dag,
)

DesplegarApiV1 = BashOperator(
    task_id='desplegar_api_v1',
    depends_on_past=True,
    bash_command='cd /tmp/CloudComputing-Servicios_y_Aplicaciones-master/practica2/docker && docker-compose up -d apiv1',
    dag=dag,
)

DesplegarApiV2 = BashOperator(
    task_id='desplegar_api_v2',
    depends_on_past=False,
    bash_command='cd /tmp/CloudComputing-Servicios_y_Aplicaciones-master/practica2/docker && docker-compose up -d apiv2',
    dag=dag,
)

TestApiV1 = BashOperator(
    task_id='test_api_v1',
    depends_on_past=True,
    bash_command='pytest /tmp/CloudComputing-Servicios_y_Aplicaciones-master/practica2/api/v1/test_apiv1.py',
    dag=dag,
)

DesplegarNginx = BashOperator(
    task_id='desplegar_nginx',
    depends_on_past=True,
    bash_command='cd /tmp/CloudComputing-Servicios_y_Aplicaciones-master/practica2/docker && docker-compose up -d nginx',
    dag=dag,
)



# Dependencias
[DescargarDatosHumedad, DescargarDatosTemperatura] >>  DescomprimirDatos >>  PrepararDatos 
PrepararDatos >> DesplegarContenedorMongo >> InsertarDatosMongo
DescargarFuenteGithub >> [DesplegarContenedorMongo, DesplegarApiV2]
InsertarDatosMongo >> TestApiV1 >> DesplegarApiV1
[DesplegarApiV1, DesplegarApiV2] >> DesplegarNginx

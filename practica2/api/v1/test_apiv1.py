import unittest, json, requests

url = 'http://localhost:8080'

class TestAPIv1 (unittest.TestCase):

    def test_humidity_24_500_elements(self):
        response = requests.get(url + '/prediction/predict/humidity/hours/24/elements/500')
        self.assertEqual('elements' in response.json(), True, "Aparece número de elementos en la respuesta")
        self.assertEqual('hours' in response.json(), True, "Aparece número de horas en la respuesta")
        self.assertEqual('predict' in response.json(), True, "Aparece el elemento a predecir en la respuesta")
        self.assertEqual('prediction' in response.json(), True, "Aparece la predicción en la respuesta")
        self.assertEqual(response.status_code,200, "Código correcto")
        self.assertEqual(response.json()['predict'], "humidity", "Elemento a predecir correcto")
        self.assertEqual(response.json()['elements'], 500, "Número de elementos de entrenamiento correctos")
        self.assertEqual(response.json()['hours'], 24, "Número de horas correctas")
        self.assertEqual(len(response.json()['prediction']), 24, "Número de predicciones correctas")

    def test_humidity_24_1000_elements(self):
        response = requests.get(url + '/prediction/predict/humidity/hours/24/elements/1000')
        self.assertEqual('elements' in response.json(), True, "Aparece número de elementos en la respuesta")
        self.assertEqual('hours' in response.json(), True, "Aparece número de horas en la respuesta")
        self.assertEqual('predict' in response.json(), True, "Aparece el elemento a predecir en la respuesta")
        self.assertEqual('prediction' in response.json(), True, "Aparece la predicción en la respuesta")
        self.assertEqual(response.status_code,200, "Código correcto")
        self.assertEqual(response.json()['predict'], "humidity", "Elemento a predecir correcto")
        self.assertEqual(response.json()['elements'], 1000, "Número de elementos de entrenamiento correctos")
        self.assertEqual(response.json()['hours'], 24, "Número de horas correctas")
        self.assertEqual(len(response.json()['prediction']), 24, "Número de predicciones correctas")

    def test_humidity_48_500_elements(self):
        response = requests.get(url + '/prediction/predict/humidity/hours/48/elements/500')
        self.assertEqual('elements' in response.json(), True, "Aparece número de elementos en la respuesta")
        self.assertEqual('hours' in response.json(), True, "Aparece número de horas en la respuesta")
        self.assertEqual('predict' in response.json(), True, "Aparece el elemento a predecir en la respuesta")
        self.assertEqual('prediction' in response.json(), True, "Aparece la predicción en la respuesta")
        self.assertEqual(response.status_code,200, "Código correcto")
        self.assertEqual(response.json()['predict'], "humidity", "Elemento a predecir correcto")
        self.assertEqual(response.json()['elements'], 500, "Número de elementos de entrenamiento correctos")
        self.assertEqual(response.json()['hours'], 48, "Número de horas correctas")
        self.assertEqual(len(response.json()['prediction']), 48, "Número de predicciones correctas")

    def test_humidity_72_500_elements(self):
        response = requests.get(url + '/prediction/predict/humidity/hours/72/elements/500')
        self.assertEqual('elements' in response.json(), True, "Aparece número de elementos en la respuesta")
        self.assertEqual('hours' in response.json(), True, "Aparece número de horas en la respuesta")
        self.assertEqual('predict' in response.json(), True, "Aparece el elemento a predecir en la respuesta")
        self.assertEqual('prediction' in response.json(), True, "Aparece la predicción en la respuesta")
        self.assertEqual(response.status_code,200, "Código correcto")
        self.assertEqual(response.json()['predict'], "humidity", "Elemento a predecir correcto")
        self.assertEqual(response.json()['elements'], 500, "Número de elementos de entrenamiento correctos")
        self.assertEqual(response.json()['hours'], 72, "Número de horas correctas")
        self.assertEqual(len(response.json()['prediction']), 72, "Número de predicciones correctas")

    def test_temperature_24_500_elements(self):
        response = requests.get(url + '/prediction/predict/temperature/hours/24/elements/500')
        self.assertEqual('elements' in response.json(), True, "Aparece número de elementos en la respuesta")
        self.assertEqual('hours' in response.json(), True, "Aparece número de horas en la respuesta")
        self.assertEqual('predict' in response.json(), True, "Aparece el elemento a predecir en la respuesta")
        self.assertEqual('prediction' in response.json(), True, "Aparece la predicción en la respuesta")
        self.assertEqual(response.status_code,200, "Código correcto")
        self.assertEqual(response.json()['predict'], "temperature", "Elemento a predecir correcto")
        self.assertEqual(response.json()['elements'], 500, "Número de elementos de entrenamiento correctos")
        self.assertEqual(response.json()['hours'], 24, "Número de horas correctas")
        self.assertEqual(len(response.json()['prediction']), 24, "Número de predicciones correctas")

    def test_temperature_24_1000_elements(self):
        response = requests.get(url + '/prediction/predict/temperature/hours/24/elements/1000')
        self.assertEqual('elements' in response.json(), True, "Aparece número de elementos en la respuesta")
        self.assertEqual('hours' in response.json(), True, "Aparece número de horas en la respuesta")
        self.assertEqual('predict' in response.json(), True, "Aparece el elemento a predecir en la respuesta")
        self.assertEqual('prediction' in response.json(), True, "Aparece la predicción en la respuesta")
        self.assertEqual(response.status_code,200, "Código correcto")
        self.assertEqual(response.json()['predict'], "temperature", "Elemento a predecir correcto")
        self.assertEqual(response.json()['elements'], 1000, "Número de elementos de entrenamiento correctos")
        self.assertEqual(response.json()['hours'], 24, "Número de horas correctas")
        self.assertEqual(len(response.json()['prediction']), 24, "Número de predicciones correctas")

    def test_temperature_48_500_elements(self):
        response = requests.get(url + '/prediction/predict/temperature/hours/48/elements/500')
        self.assertEqual('elements' in response.json(), True, "Aparece número de elementos en la respuesta")
        self.assertEqual('hours' in response.json(), True, "Aparece número de horas en la respuesta")
        self.assertEqual('predict' in response.json(), True, "Aparece el elemento a predecir en la respuesta")
        self.assertEqual('prediction' in response.json(), True, "Aparece la predicción en la respuesta")
        self.assertEqual(response.status_code,200, "Código correcto")
        self.assertEqual(response.json()['predict'], "temperature", "Elemento a predecir correcto")
        self.assertEqual(response.json()['elements'], 500, "Número de elementos de entrenamiento correctos")
        self.assertEqual(response.json()['hours'], 48, "Número de horas correctas")
        self.assertEqual(len(response.json()['prediction']), 48, "Número de predicciones correctas")

    def test_temperature_72_500_elements(self):
        response = requests.get(url + '/prediction/predict/temperature/hours/72/elements/500')
        self.assertEqual('elements' in response.json(), True, "Aparece número de elementos en la respuesta")
        self.assertEqual('hours' in response.json(), True, "Aparece número de horas en la respuesta")
        self.assertEqual('predict' in response.json(), True, "Aparece el elemento a predecir en la respuesta")
        self.assertEqual('prediction' in response.json(), True, "Aparece la predicción en la respuesta")
        self.assertEqual(response.status_code,200, "Código correcto")
        self.assertEqual(response.json()['predict'], "temperature", "Elemento a predecir correcto")
        self.assertEqual(response.json()['elements'], 500, "Número de elementos de entrenamiento correctos")
        self.assertEqual(response.json()['hours'], 72, "Número de horas correctas")
        self.assertEqual(len(response.json()['prediction']), 72, "Número de predicciones correctas")
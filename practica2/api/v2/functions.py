from urllib.request import urlopen
from xml.dom import minidom

# Este método tomará los datos de http://www.aemet.es/xml/municipios_h/localidad_h_18087.xml
# y creará un diccionario con ellos.
def getData():
    var_url = urlopen("http://www.aemet.es/xml/municipios_h/localidad_h_18087.xml")
    xmldoc = minidom.parse(var_url)
    
    response = {}

    for dia in xmldoc.getElementsByTagName("dia"):
        fecha = dia.getAttribute('fecha')

        temperaturas_xml = dia.getElementsByTagName("temperatura")
        temperaturas = []
        horas = [] 
        for temp in temperaturas_xml:
            horas.append(temp.getAttribute('periodo'))
            temperaturas.append(temp.firstChild.data)

        humedad_xml = dia.getElementsByTagName("humedad_relativa")
        humedad = []
        for hum in humedad_xml:
            humedad.append(hum.firstChild.data)

        response[fecha] = []
        for i in range(len(horas)):
            h = horas[i] + ":00"
            response[fecha].append({"hour": h, "temp": temperaturas[i], "hum": humedad[i]})

    return response
import unittest, json, requests

url = 'http://localhost:8080'

from apiv1 import app

class TestAPIv1 (unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_obtener_prediccion_24(self):
        result = self.app.get(url + '/servicio/v1/prediccion/24')
        self.assertEqual(result.status_code, 200, "Estado correcto")
        self.assertEqual(type(result.json), list, "Devuelve una lista")
        self.assertEqual(len(result.json), 24, "Devuelve la prediccion de 24 horas")

    def test_obtener_prediccion_48(self):
        result = self.app.get(url + '/servicio/v1/prediccion/48')
        self.assertEqual(result.status_code, 200, "Estado correcto")
        self.assertEqual(type(result.json), list, "Devuelve una lista")
        self.assertEqual(len(result.json), 48, "Devuelve la prediccion de 48 horas")

    def test_obtener_prediccion_72(self):
        result = self.app.get(url + '/servicio/v1/prediccion/72')
        self.assertEqual(result.status_code, 200, "Estado correcto")
        self.assertEqual(type(result.json), list, "Devuelve una lista")
        self.assertEqual(len(result.json), 72, "Devuelve la prediccion de 72 horas")
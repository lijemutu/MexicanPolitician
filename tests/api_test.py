from ast import Assert
import unittest

from itsdangerous import json

from APIs.names_api import NamesApi

class TestSuite(unittest.TestCase):

    def test_NamesApi(self):
        # Código que se quiere probar
        name = "Andres"
        lastName = "López"
        secondLastName = "Obrador"

        nationality = NamesApi(name,lastName,secondLastName=secondLastName)
        jsonResponse = nationality.requestFullName()

        self.assertNotEqual(jsonResponse,{})

    def test_NamesApiPartial(self):
        name = "Andres"
        nationality = NamesApi(name)
        jsonResponse = nationality.requestPartialName("forename")

        self.assertNotEqual(jsonResponse,{})


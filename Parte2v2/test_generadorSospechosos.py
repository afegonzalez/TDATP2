from unittest import TestCase
from GeneradorSospechosos import GeneradorSospechosos
from Persona import Persona

class TestGeneradorSospechosos(TestCase):
    def test01NoEncuentraSospechososEnListaMenorA5(self):
        persona1 = Persona("Carlos", 1, 50)
        persona2 = Persona("Juan", 2, 15)
        persona3 = Persona("Esteban", 3, 35)


        listaDePersonas = []

        listaDePersonas.append(persona1)
        listaDePersonas.append(persona2)
        listaDePersonas.append(persona3)

        generadorSospechosos = GeneradorSospechosos(listaDePersonas)


        listaSospechosos = generadorSospechosos.encontrarSospechosos()

        self.assertTrue(len(listaSospechosos) == 0)

    def test02EncuentraSospechososEnListaIgualA5(self):
        persona1 = Persona("Carlos", 1, 50)
        persona2 = Persona("Juan", 2, 15)
        persona3 = Persona("Esteban", 3, 35)
        persona4 = Persona("Mario", 4, 15)
        persona5 = Persona("Lucas", 5, 25)


        listaDePersonas = []

        listaDePersonas.append(persona1)
        listaDePersonas.append(persona2)
        listaDePersonas.append(persona3)
        listaDePersonas.append(persona4)
        listaDePersonas.append(persona5)

        generadorSospechosos = GeneradorSospechosos(listaDePersonas)

        listaSospechosos = generadorSospechosos.encontrarSospechosos()

        self.assertTrue(len(listaSospechosos) == 1)

    def test03NoEncuentraSospechososEnListaIgualA5PorqueSeRepiteUno(self):
        persona1 = Persona("Carlos", 1, 50)
        persona2 = Persona("Juan", 2, 15)
        persona3 = Persona("Esteban", 3, 35)
        persona4 = Persona("Mario", 4, 15)
        persona5 = Persona("Carlos", 5, 25)


        listaDePersonas = []

        listaDePersonas.append(persona1)
        listaDePersonas.append(persona2)
        listaDePersonas.append(persona3)
        listaDePersonas.append(persona4)
        listaDePersonas.append(persona5)

        generadorSospechosos = GeneradorSospechosos(listaDePersonas)

        listaSospechosos = generadorSospechosos.encontrarSospechosos()

        self.assertTrue(len(listaSospechosos) == 0)

    def test04NoEncuentraSospechososEnListaIgualA5PorqueSeRepiteMasDeUno(self):
        persona1 = Persona("Carlos", 1, 50)
        persona2 = Persona("Juan", 2, 15)
        persona3 = Persona("Esteban", 3, 35)
        persona4 = Persona("Mario", 4, 15)
        persona5 = Persona("Carlos", 5, 25)
        persona6 = Persona("Mario", 4, 25)

        listaDePersonas = []

        listaDePersonas.append(persona1)
        listaDePersonas.append(persona2)
        listaDePersonas.append(persona3)
        listaDePersonas.append(persona4)
        listaDePersonas.append(persona5)
        listaDePersonas.append(persona6)


        generadorSospechosos = GeneradorSospechosos(listaDePersonas)

        listaSospechosos = generadorSospechosos.encontrarSospechosos()

        self.assertTrue(len(listaSospechosos) == 0)

    def test05EncuentraSospechososConUnoQueEntraYSale(self):
        persona1 = Persona("Carlos", 1, 50)
        persona2 = Persona("Juan", 2, 15)
        persona3 = Persona("Esteban", 3, 35)
        persona4 = Persona("Mario", 4, 15)
        persona5 = Persona("Carlos", 5, 25)
        persona6 = Persona("Mauro", 6, 15)


        listaDePersonas = []

        listaDePersonas.append(persona1)
        listaDePersonas.append(persona2)
        listaDePersonas.append(persona3)
        listaDePersonas.append(persona4)
        listaDePersonas.append(persona5)
        listaDePersonas.append(persona6)


        generadorSospechosos = GeneradorSospechosos(listaDePersonas)

        listaSospechosos = generadorSospechosos.encontrarSospechosos()

        self.assertTrue(len(listaSospechosos) == 2)

    def test06EncuentraSospechososConUnoQueEntraYSale(self):
        persona1 = Persona("Carlos", 1, 50)
        persona2 = Persona("Juan", 2, 15)
        persona3 = Persona("Esteban", 3, 35)
        persona4 = Persona("Mario", 4, 15)
        persona5 = Persona("Carlos", 5, 25)
        persona6 = Persona("Mauro", 6, 15)


        listaDePersonas = []

        listaDePersonas.append(persona1)
        listaDePersonas.append(persona2)
        listaDePersonas.append(persona3)
        listaDePersonas.append(persona4)
        listaDePersonas.append(persona5)
        listaDePersonas.append(persona6)


        generadorSospechosos = GeneradorSospechosos(listaDePersonas)

        listaSospechosos = generadorSospechosos.encontrarSospechosos()

        self.assertTrue(len(listaSospechosos) == 2)
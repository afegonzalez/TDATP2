from unittest import TestCase
import Parte2.GeneradorSospechosos
import Parte2.Persona

class TestGeneradorSospechosos(TestCase):
    pass
    # def test01NoEncuentraSospechososEnListaMenorA5(self):
    #     persona1 = Parte2.Persona.Persona("Carlos", 1, 50)
    #     persona2 = Parte2.Persona.Persona("Juan", 2, 15)
    #     persona3 = Parte2.Persona.Persona("Esteban", 3, 35)
    #
    #
    #     listaDePersonas = []
    #
    #     listaDePersonas.append(persona1)
    #     listaDePersonas.append(persona2)
    #     listaDePersonas.append(persona3)
    #
    #     generadorSospechosos = Parte2.GeneradorSospechosos.GeneradorSospechosos(listaDePersonas)
    #
    #
    #     listaSospechosos = generadorSospechosos.encontrarSospechosos()
    #
    #     self.assertTrue(len(listaSospechosos) == 0)
    #
    # def test02EncuentraSospechososEnListaIgualA5(self):
    #     persona1 = Parte2.Persona.Persona("Carlos", 1, 50)
    #     persona2 = Parte2.Persona.Persona("Juan", 2, 15)
    #     persona3 = Parte2.Persona.Persona("Esteban", 3, 35)
    #     persona4 = Parte2.Persona.Persona("Mario", 4, 15)
    #     persona5 = Parte2.Persona.Persona("Lucas", 5, 25)
    #
    #
    #     listaDePersonas = []
    #
    #     listaDePersonas.append(persona1)
    #     listaDePersonas.append(persona2)
    #     listaDePersonas.append(persona3)
    #     listaDePersonas.append(persona4)
    #     listaDePersonas.append(persona5)
    #
    #     generadorSospechosos = Parte2.GeneradorSospechosos.GeneradorSospechosos(listaDePersonas)
    #
    #     listaSospechosos = generadorSospechosos.encontrarSospechosos()
    #
    #     self.assertTrue(len(listaSospechosos) == 1)
    #
    # def test03NoEncuentraSospechososEnListaIgualA5PorqueSeRepiteUno(self):
    #     persona1 = Parte2.Persona.Persona("Carlos", 1, 50)
    #     persona2 = Parte2.Persona.Persona("Juan", 2, 15)
    #     persona3 = Parte2.Persona.Persona("Esteban", 3, 35)
    #     persona4 = Parte2.Persona.Persona("Mario", 4, 15)
    #     persona5 = Parte2.Persona.Persona("Carlos", 5, 25)
    #
    #
    #     listaDePersonas = []
    #
    #     listaDePersonas.append(persona1)
    #     listaDePersonas.append(persona2)
    #     listaDePersonas.append(persona3)
    #     listaDePersonas.append(persona4)
    #     listaDePersonas.append(persona5)
    #
    #     generadorSospechosos = Parte2.GeneradorSospechosos.GeneradorSospechosos(listaDePersonas)
    #
    #     listaSospechosos = generadorSospechosos.encontrarSospechosos()
    #
    #     self.assertTrue(len(listaSospechosos) == 0)
    #
    # def test04NoEncuentraSospechososEnListaIgualA5PorqueSeRepiteMasDeUno(self):
    #     persona1 = Parte2.Persona.Persona("Carlos", 1, 50)
    #     persona2 = Parte2.Persona.Persona("Juan", 2, 15)
    #     persona3 = Parte2.Persona.Persona("Esteban", 3, 35)
    #     persona4 = Parte2.Persona.Persona("Mario", 4, 15)
    #     persona5 = Parte2.Persona.Persona("Carlos", 5, 25)
    #     persona6 = Parte2.Persona.Persona("Mario", 4, 25)
    #
    #     listaDePersonas = []
    #
    #     listaDePersonas.append(persona1)
    #     listaDePersonas.append(persona2)
    #     listaDePersonas.append(persona3)
    #     listaDePersonas.append(persona4)
    #     listaDePersonas.append(persona5)
    #     listaDePersonas.append(persona6)
    #
    #
    #     generadorSospechosos = Parte2.GeneradorSospechosos.GeneradorSospechosos(listaDePersonas)
    #
    #     listaSospechosos = generadorSospechosos.encontrarSospechosos()
    #
    #     self.assertTrue(len(listaSospechosos) == 0)
    #
    # def test05EncuentraSospechososConUnoQueEntraYSale(self):
    #     persona1 = Parte2.Persona.Persona("Carlos", 1, 50)
    #     persona2 = Parte2.Persona.Persona("Juan", 2, 15)
    #     persona3 = Parte2.Persona.Persona("Esteban", 3, 35)
    #     persona4 = Parte2.Persona.Persona("Mario", 4, 15)
    #     persona5 = Parte2.Persona.Persona("Carlos", 5, 25)
    #     persona6 = Parte2.Persona.Persona("Mauro", 6, 15)
    #
    #
    #     listaDePersonas = []
    #
    #     listaDePersonas.append(persona1)
    #     listaDePersonas.append(persona2)
    #     listaDePersonas.append(persona3)
    #     listaDePersonas.append(persona4)
    #     listaDePersonas.append(persona5)
    #     listaDePersonas.append(persona6)
    #
    #
    #     generadorSospechosos = Parte2.GeneradorSospechosos.GeneradorSospechosos(listaDePersonas)
    #
    #     listaSospechosos = generadorSospechosos.encontrarSospechosos()
    #
    #     self.assertTrue(len(listaSospechosos) == 2)
    #
    # def test06EncuentraSospechososConUnoQueEntraYSale(self):
    #     persona1 = Parte2.Persona.Persona("Carlos", 1, 50)
    #     persona2 = Parte2.Persona.Persona("Juan", 2, 15)
    #     persona3 = Parte2.Persona.Persona("Esteban", 3, 35)
    #     persona4 = Parte2.Persona.Persona("Mario", 4, 15)
    #     persona5 = Parte2.Persona.Persona("Carlos", 5, 25)
    #     persona6 = Parte2.Persona.Persona("Mauro", 6, 15)
    #
    #
    #     listaDePersonas = []
    #
    #     listaDePersonas.append(persona1)
    #     listaDePersonas.append(persona2)
    #     listaDePersonas.append(persona3)
    #     listaDePersonas.append(persona4)
    #     listaDePersonas.append(persona5)
    #     listaDePersonas.append(persona6)
    #
    #
    #     generadorSospechosos = Parte2.GeneradorSospechosos.GeneradorSospechosos(listaDePersonas)
    #
    #     listaSospechosos = generadorSospechosos.encontrarSospechosos()
    #
    #     self.assertTrue(len(listaSospechosos) == 2)
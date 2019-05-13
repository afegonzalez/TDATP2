from Persona import Persona


class GeneradorSospechosos:
    def __init__(self, listaIngresos):
        self.listaIngresos = listaIngresos

    def encontrarSospechosos(self):
        lista_de_sospechosos = []

        print(len(self.listaIngresos))

        lista_entradas = self.listaIngresos

        lista_entradas = (self.listaIngresos).copy()

        self.listaIngresos.sort(key=lambda x: x.hora_salida, reverse=True)

        lista_salidas = (self.listaIngresos).copy()

        lista_auxiliar = []

        for candidatos in lista_entradas:
            if(candidatos.tiempototal > 40):
                lista_auxiliar.append(candidatos)






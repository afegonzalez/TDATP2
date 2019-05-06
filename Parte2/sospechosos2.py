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


        for primer_complice in lista_entradas:
            tiempo_inicio = primer_complice.ingreso
            tiempo_salida = primer_complice.hora_salida
            tiempo_ilicito = primer_complice.tiempototal

            for candidato in lista_salidas:
                if(candidato.hora_salida - tiempo_inicio < 40):  # descarta candidato y todos los que le sigan si el tiempo es menor a 40
                    break
                    
                if candidato.hora_salida - tiempo_inicio < tiempo_ilicito:
                    tiempo_ilicito = candidato.hora_salida - tiempo_inicio
                    lista_auxiliar.append(candidato)
                    primero_en_salir = candidato

                elif candidato.hora_salida - tiempo_inicio >= tiempo_ilicito:
                    lista_auxiliar.append(candidato)

                elif candidato.nombre == primer_complice.nombre:  #si el candidato es el primer complice, significa que salio y entro -> pasar a la siguiente iteracion
                    lista_auxiliar = []
                    break

                elif candidato 

                #elif que analiza cuando estan todos dentro

            if len(lista_auxiliar) >= 5 & len(lista_auxiliar) <= 10:
                lista_de_sospechosos.append(lista_auxiliar)

        for set_sospechosos in lista_de_sospechosos:

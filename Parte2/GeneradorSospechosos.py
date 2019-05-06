class GeneradorSospechosos:

    def __init__(self, listaIngresos):
        self.listaIngresos = listaIngresos


    def encontrarSospechosos(self):
        lista_de_listas = []
        print(len(self.listaIngresos))
        lista_entradas = (self.listaIngresos).copy()
        self.listaIngresos.sort(key=lambda x: x.hora_salida, reverse=True)
        lista_salidas = (self.listaIngresos).copy()
        sospechosos_actuales = []


        for primer_complice in lista_entradas:
            primero_en_salir = primer_complice
            tiempo_inicio = primer_complice.ingreso
            tiempo_ilicito = primer_complice.tiempototal

            for candidato in lista_salidas:
                if candidato.hora_salida - tiempo_inicio < 40:  # descarta candidato y todos los que le sigan si el tiempo es menor a 40
                    break
                if candidato.ingreso > primero_en_salir.hora_salida:
                    break                                       # no comparte tiempo con el que se lleva el botin, no esta en la banda
                if candidato.ingreso > tiempo_inicio + 120:
                    break                                       # el robo dura 120 minutos maximo

                if candidato.hora_salida - tiempo_inicio < tiempo_ilicito:
                    tiempo_ilicito = candidato.hora_salida - tiempo_inicio
                    sospechosos_actuales.append(candidato)
                    primero_en_salir = candidato

                elif candidato.hora_salida - tiempo_inicio >= tiempo_ilicito:
                    sospechosos_actuales.append(candidato)

            if len(sospechosos_actuales) >= 5 & len(sospechosos_actuales) <= 10:
                lista_de_listas.append(sospechosos_actuales)

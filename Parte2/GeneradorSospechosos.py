class GeneradorSospechosos:

    def __init__(self, listaIngresos):
        self.listaIngresos = listaIngresos

    def encontrarSospechosos(self):

        lista = self.listaIngresos

        index = len(lista)

        listaSospechosos = []

        tiempoAnterior = 0

        tiempoTotalMaximo = 0

        indice = 1

        egresoAnt = 0

        for j in range(len(lista)):
            posibleSospechosos = []

            if (lista[j].tiempototal < 120):
                posibleSospechosos.append(lista[j])
                egresoMasTemprano = lista[j].hora_salida
                for x in range(j + 1, len(lista)):
                    if (lista[x].tiempototal < 120 and lista[x].ingreso < egresoMasTemprano
                        and len(posibleSospechosos) < 10):
                        if (egresoMasTemprano > lista[x].hora_salida):
                            egresoMasTemprano = lista[x].hora_salida
                        if (lista[x] in posibleSospechosos):
                            indice = posibleSospechosos.index(lista[x])
                            posibleSospechosos[indice].tiempototal += lista[x].tiempototal
                        else:
                            posibleSospechosos.append(lista[x])
                if (len(posibleSospechosos) >= 5):
                    listaSospechosos.append(posibleSospechosos)
                egresoMasTemprano = 0

        return listaSospechosos
    
    
    #lista_entradas menor a mayor
#lista_salidas menor a mayor

#para cada i en lista_entradas:

	#sea tiempo_inicio = tiempo de entrada de i
	#sea tiempo_salida = tiempo de entrada de i
	#tiempo_ilicito = tiempo_salida - tiempo_entrada

	#para cada j en lista_salidas:
		#si tiempo_salida_j - tiempo_inicio < 40:
			# candidato j es descartado
		#si tiempo_salida_j - tiempo_inicio < tiempo_ilicito:
			#tiempo_ilicito = tiempo_salida_j - tiempo_inicio
			#insertar j en candidatos (pasa a ser el primero en salir)

		#si tiempo_salida_j - tiempo_inicio >= tiempo ilicito:
			#insertar j en candidatos (todos aquellos que esten dsp de que sale el primero son de la banda)

		#sea ultimo_en_entrar el tiempo en el que ingreso el ultimo sin que nadie de los candidatos saliera(?)
		#si tiempo_salida_j <= ultimo_en_entrar:
			#insertar j en candidatos

		#si j en lista_candidatos o j == i (hacer algo)-----------------_> no me acuerdo como era este caso
			#algo

	#si lista de candidatos < 5:
		#nada
	#si lista de candidatos > 10: (creo que esta no deberia pasar de ninguna forma, si pasara habria que separar los grupos)

	#else:
		#meter lista de candidatos



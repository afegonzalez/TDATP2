class GeneradorSospechosos:

    def __init__(self, listaIngresos):
        self.listaIngresos = listaIngresos

    def encontrarSospechosos(self):
		lista_de_sospechosos = []
		lista_entradas = lista_de_sospechosos.sort(key=sortByEntrance) #hay que crear metodos sort by entrance y exit
		lista_salidas = lista_de_sospechosos.sort(key=sortByExit)	   #son simplemente getters de tiempo de salida y entrada
		lista_auxiliar = []

		for primer_complice in lista_entradas:
			tiempo_inicio = primer_complice.ingreso
			tiempo_salida = primer_complice.hora_salida
			tiempo_ilicito = primer_complice.tiempototal

			for candidato in lista_salidas:
				if not (candidato.hora_salida - tiempo_inicio < 40): #descarta candidato si el tiempo es menor a 40
					if tiempo_salida_j - tiempo_inicio < tiempo_ilicito:
						tiempo_ilicito = tiempo_salida_j - tiempo_inicio
						lista_auxiliar.append(candidato)
						primero_en_salir = candidato

					if tiempo_salida_j - tiempo_inicio >= tiempo_ilicito:
						lista_auxiliar.append(candidato)

					if candidato.nombre == primer_complice.nombre: #pasar a la siguiente iteracion
						lista_auxiliar = []
						break

			if len(lista_auxiliar) >= 5 & len(lista_auxiliar) <= 10:
				lista_de_sospechosos.append(lista_auxiliar)


					


    
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



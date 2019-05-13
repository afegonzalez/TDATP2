from Persona import Persona1


def encontrarSospechosos(lista):

    index = len(lista)

    listaSospechosos = []




    tiempoAnterior = 0

    tiempoTotalMaximo = 0

    indice = 1

    egresoAnt = 0



    for j in range(len(lista)):
        posibleSospechosos = []

        if(lista[j].tiempototal < 120):
            posibleSospechosos.append(lista[j])
            egresoMasTemprano = lista[j].hora_salida
            for x in range(j+1,len(lista)):
                if(lista[x].tiempototal < 120 and lista[x].ingreso < egresoMasTemprano
                    and len(posibleSospechosos) < 10):
                    if(egresoMasTemprano > lista[x].hora_salida):
                        egresoMasTemprano = lista[x].hora_salida
                    if(lista[x] in posibleSospechosos):
                        indice = posibleSospechosos.index(lista[x])
                        posibleSospechosos[indice].tiempototal += lista[x].tiempototal
                    else:
                        posibleSospechosos.append(lista[x])
            if(len(posibleSospechosos) >= 5):
                listaSospechosos.append(posibleSospechosos)
            egresoMasTemprano = 0




    return listaSospechosos



def generarPersonas(nombreaArchivo):
    archivo = open(nombreaArchivo, 'r')

    listaPersonas = []

    lineas = archivo.read().splitlines()

    for elemento in lineas:
        linea1 = elemento.split(",")
        personaAux = Persona1(linea1[0],linea1[1],linea1[2])
        listaPersonas.append(personaAux)

    archivo.close()

    return listaPersonas

def generarArchivoSalida(listaDeListas):

    with open('sospechosos.txt', 'w') as f:
        for lista in listaDeListas:
            for elemento in lista:
                f.write(elemento.nombre + "," + str(elemento.tiempototal)),
                f.write('\n')
            f.write('\n')



def main(archivo):



    lista = generarPersonas(archivo)

    generarArchivoSalida(encontrarSospechosos(lista)
)


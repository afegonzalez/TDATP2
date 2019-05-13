import sys
from Persona import Persona
from GeneradorSospechosos import GeneradorSospechosos





def generarPersonas(nombreaArchivo):
    archivo = open(nombreaArchivo, 'r')

    listaPersonas = []

    lineas = archivo.read().splitlines()

    for elemento in lineas:
        linea1 = elemento.split(",")
        personaAux = Persona(linea1[0],linea1[1],linea1[2])
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

def sospechoso(listaEntrada,listaSalida):
    ant = 0
    listaAux = []
    horaSalidaAnt = 0
    for x in range (len(listaSalida) - 1):
        if(listaSalida[x].ingreso > ant and listaSalida[x].tiempototal > 40 and listaSalida[x].tiempototal >= horaSalidaAnt):
            listaAux.append(listaSalida[x])
            ant = listaSalida[x].hora_salida
    return listaAux

def main():
    persona1 = Persona("Carlos", 0, 50)
    persona2 = Persona("Juan", 15, 45)
    persona3 = Persona("Esteban", 30, 30)
    persona4 = Persona("Mario", 30, 15)
    persona5 = Persona("Lucas", 30, 15)
    persona6 = Persona("Mauro", 35, 10)
    persona7 = Persona("Jose", 1, 110)



    listaDePersonas = []

    listaDePersonas.append(persona1)
    listaDePersonas.append(persona2)
    listaDePersonas.append(persona3)
    listaDePersonas.append(persona4)
    listaDePersonas.append(persona5)
    listaDePersonas.append(persona6)
    listaDePersonas.append(persona7)



    lista_entradas = (listaDePersonas).copy()

    listaDePersonas.sort(key=lambda x: x.hora_salida, reverse=False)

    lista_salidas = (listaDePersonas).copy()

    lista = sospechoso(lista_entradas,lista_salidas)


    for elemento in lista_salidas:
        print(elemento)

main()

"""
    listaPersonas = generarPersonas(argv)


    generadorSospechosos = GeneradorSospechosos(listaPersonas)

    listaSospechosos = generadorSospechosos.encontrarSospechosos()


    generarArchivoSalida(listaSospechosos)


if __name__ == "__main__":
   main(sys.argv[1])"""

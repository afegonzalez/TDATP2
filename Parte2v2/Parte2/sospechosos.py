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



def main():
    persona1 = Persona("Carlos", 1, 50)
    persona2 = Persona("Juan", 2, 15)
    persona3 = Persona("Esteban", 3, 35)
    persona4 = Persona("Mario", 4, 15)
    persona5 = Persona("Lucas", 5, 25)
    persona6 = Persona("Mauro", 6, 15)

    listaDePersonas = []

    listaDePersonas.append(persona1)
    listaDePersonas.append(persona2)
    listaDePersonas.append(persona3)
    listaDePersonas.append(persona4)
    listaDePersonas.append(persona5)
    listaDePersonas.append(persona6)


    lista_entradas = (listaDePersonas).copy()

    listaDePersonas.sort(key=lambda x: x.hora_salida, reverse=True)

    lista_salidas = (listaDePersonas).copy()


    for elemento in lista_entradas:
        print(lista_entradas)

main()

"""
    listaPersonas = generarPersonas(argv)


    generadorSospechosos = GeneradorSospechosos(listaPersonas)

    listaSospechosos = generadorSospechosos.encontrarSospechosos()


    generarArchivoSalida(listaSospechosos)


if __name__ == "__main__":
   main(sys.argv[1])"""

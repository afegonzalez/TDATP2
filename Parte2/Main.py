import sys
import Parte2.Persona
import Parte2.GeneradorSospechosos

def generarPersonas(nombreaArchivo):
    archivo = open(nombreaArchivo, 'r')
    listaPersonas = []
    lineas = archivo.read().splitlines()

    for elemento in lineas:
        linea1 = elemento.split(",")
        personaAux = Parte2.Persona.Persona(linea1[0],linea1[1],linea1[2])
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


def main(argv):
    listaPersonas = generarPersonas(argv)
    generadorSospechosos = Parte2.GeneradorSospechosos.GeneradorSospechosos(listaPersonas)
    listaSospechosos = generadorSospechosos.encontrarSospechosos()
    generarArchivoSalida(listaSospechosos)


if __name__ == "__main__":
    main(sys.argv[1])

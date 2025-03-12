def buscarPalabra(objetivo, palabras):


    while True: 
        salida = "exit"
        palabras = str("Buscar nombre:"+ str(input))
        if (objetivo == palabras): 
            return True
        elif (palabras == salida):
            print("FIN DEL PROGRAMA")

def imprimirListaInversa(lista):
    return lista[:: -1]

nombres = ["Mengano", "Fulano", "Zutano", "Perantano"]
edades = {
    "Mengano": 0,
    "Fulano": 25,
    "Zutano": 50,
    "Perantano": 75
}

print(imprimirListaInversa(nombres))


nombre = "Mengano"
# el usuario te da la palabra
if buscarPalabra(nombre,nombres) == True: 
    print(str(edades))
    # le paso la palabra, y me devuelve si esta o no
    
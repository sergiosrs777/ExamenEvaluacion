def buscarPalabra(objetivo, palabras):
    for x in palabras:
        if x == objetivo:
            return True
    
    return False

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

while True:
    nombre = str(input("Buscar nombre: "))
    if buscarPalabra(nombre,nombres) == True: 
        print("La palabra existe")
    elif (nombre == "exit"):
        print("FIN DEL PROGRAMA")    
    else:
        print("No existe")
    
    
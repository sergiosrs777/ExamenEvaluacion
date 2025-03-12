# Examen evaluacion

1. [Invertir Lista](#invertir)
2. [Buscar Palabra](#buscar)
3. [Codigo Lista](#mostrar)
4. [Codigo Busqueda](#codigo)


<div id= invertir></div>

# 1. Invertir lista
Para invertir la lista en la funcion ya definida la pasamos el parametro ya definido y que lo devuelva empezando por el final.

```python
def imprimirListaInversa(lista):
    return lista[:: -1]
```

<div id= buscar></div>

# 2. Buscar Palabras 

Para buscar las palabras y que sean iguales hay que comparar los dos parametros ya dados con un `if` y que si son iguales te devuelvan `true` o te siga pidiendo nombres hasta que se de con el nombre o exit para salir del programa
```python
def buscarPalabra(objetivo, palabras):
    for x in palabras:
        if x == objetivo:
            return True
    
    return False
```

<div id= mostrar></div>

# 3. Codigo lista
El codigo para que se muestre una lista invertida es `print` para mostrar 
el nombre de la funcion ***imprimirListaInversa*** y como parametro se le pasa una lista
```python 
print(imprimirListaInversa(nombres))
```

<div id = codigo></div>

# 4. Codigo buscar palabra
Para buscar palabra y que coincidan en un bucle se le pide una palabra y se le pasa una lista y si el nombre coincide con el objetivo se muestra *el nombre existe*  si es exit que finalice el programa
```python
while True:
    nombre = str(input("Buscar nombre: "))
    if buscarPalabra(nombre,nombres) == True: 
        print("La palabra existe")
    elif (nombre == "exit"):
        print("FIN DEL PROGRAMA")    
    else:
        print("No existe")
```
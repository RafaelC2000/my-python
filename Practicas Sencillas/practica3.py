print("3- Definir una función que calcule la longitud de una lista o una  \n cadena dada. (Es cierto que python tiene la función len() incorporada, pero \n escribirla por nosotros mismos resulta un muy buen ejercicio.\n\n")
print("Introduce una cadena de texto")
cadena=list(input())
def largo_cadena (cadena):
    cont = 0
    for i in cadena:
        cont += 1
    return cont

print("\n La cadena mide:\n")
print(largo_cadena (cadena))

print("\n comprobacion: \n")
print(len(cadena))
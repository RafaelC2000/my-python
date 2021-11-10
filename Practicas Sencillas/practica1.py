print("1- Definir una función max_de_dos() que tome como argumento dos \n números y devuelva el mayor de ellos. (Es cierto que python tiene una \n función max() incorporada, pero hacerla nosotros mismos es un muy buen ejercicio.\n\n")
print("Introduce el primer numero:")
num1=int(input())
print("Introduce el segundo numero:")
num2=int(input())
def max_de_dos(num1,num2):
    if num1>num2:
        return num1
    if num1<num2:
        return num2
    else:
        return 0
print("El numero mayor es:\n")
print(max_de_dos(num1,num2))
print("\ncomprobacion\n")
print(max(num1,num2))
print("2- Definir una función max_de_tres(), que tome tres números como \n argumentos y devuelva el mayor de ellos. \n\n")
print("Introduce el primer numero:")
num1=int(input())
print("Introduce el segundo numero:")
num2=int(input())
print("Introduce el tercer numero:")
num3=int(input())
def max_de_tres(num1,num2,num3):
    if num1>=num2 and num1>=num3:
        return num1
    if num2>=num1 and num2>=num3:
        return num2
    if num3>=num1 and num3>=num2:
        return num3
    else:
        return 0
print("El numero mayor es:\n")
print(max_de_tres(num1,num2,num3))
print("\ncomprobacion\n")
print(max(num1,num2,num3))
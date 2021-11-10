def generarCadenas(cad, n ,tam):
    if n == tam:
        print(cad)
        return
    cad1 = cad + "0"
    cad2 = cad + "1"

    generarCadenas(cad1, n ,tam+1)
    generarCadenas(cad2, n ,tam+1)
   
n = int(input("Ingresa un N: "))
generarCadenas("",n, 0)



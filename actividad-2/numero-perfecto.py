#Escribe un programa en python que diga si un número es perfecto e imprima todos los números perfectos hasta N
#Autor: Enrique Vidó
numero = int(input("Escribe un numero: "))
divisores = []
numeros_perfectos = []

if numero < 1:
    print("El numero no es perfecto")
else:
    for i in range(1, numero):
        if numero % i == 0:
            divisores.append(i)

    if sum(divisores) == numero:
        print("El numero es perfecto")
    else:
        print("El numero no es perfecto")
    
    print("Los numeros perfectos antes del que ingresaste son: ")
    for i in range (1, numero):
        divisores = []
        for j in range (1, i):
            if i % j == 0:
                divisores.append(j)

        if sum(divisores) == i:
            numeros_perfectos.append(i) 
    print(numeros_perfectos)
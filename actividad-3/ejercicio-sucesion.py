#Escribe un programa en python que genere la sucesión para k igual a n
#Autor: Enrique Vidó
k = int(input("Introduce los términos de la sucesión que deseas ver: "))

for i in range(1, k+1):
    numerador = (-1)**(i+1)
    denominador = i**2
    if i < k:
        print (f"{numerador}/{denominador},", end=" ")
    else:
        print (f"{numerador}/{denominador}...")
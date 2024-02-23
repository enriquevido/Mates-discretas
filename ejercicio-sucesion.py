k = int(input("Introduce los términos de la sucesión que deseas ver: "))

for i in range(1, k+1):
    numerador = (-1)**(i+1)
    denominador = i**2
    if i < k:
        print (f"{numerador}/{denominador},", end=" ")
    else:
        print (f"{numerador}/{denominador}...", end=" ")
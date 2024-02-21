# -*- coding: utf-8 -*-
"""
@author: enrique

Escribe un programa que indique si un número dado es primo

"""

numero = int(input ("Escribe un numero: "))

primo = True

for i in range(2, numero // 2 + 1):
    if (numero % i == 0):
        primo: False
        break
        
if primo == True:
    print (f"El numero {numero} es primo")
else: 
    print(f"El numero {numero} no es primo")
            
print (f"Los numeros primos antes del {numero} son: ")

for i in range (2, numero // 2+1):
        if (numero % i> 0):
            print(i)
            break
        else:
            print(f"El numero {numero} no tiene numeros primos antes")

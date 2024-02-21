#Escribe un programa en python que indique si dos números dados son amigos
#Autor: Enrique Vidó
num_1 = int(input("Introduce un numero: "))
num_2 = int(input("Introduce otro numero: "))
divisores_num1 = []
divisores_num2 = []

if num_1<=0 and num_2<=0:
      print("Los numeros deben ser mayores que 0.")
else:
      for i in range(1, num_1):   
        if num_1 % i == 0:
            divisores_num1.append(i)
    
      for i in range(1, num_2):
         if num_2 % i == 0:
            divisores_num2.append(i)

      if sum(divisores_num1) == num_2 and sum(divisores_num2) == num_1:
            print("Los numeros son amigos")
      else:
            print("Los numeros no son amigos")


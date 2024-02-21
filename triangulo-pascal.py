#Escribe un programa en python que genere el triangulo de Pascal hasta n filas
#Autor: Enrique Vidó
n_filas = int(input("Escribe el número de filas que deseas visualizar: "))
fila_vieja = [1]

if n_filas < 1:
    print("Numero de filas inválido")
else:
    espacios = "\t" .expandtabs(n_filas)
    print(espacios, fila_vieja)

    for i in range(1, n_filas):
        fila_nueva = [1]

        for j in range (0, i-1):
            nuevo_valor = fila_vieja[j] + fila_vieja[j+1] 
            fila_nueva.append(nuevo_valor)

        fila_nueva.append(1)
        espacios = "\t" .expandtabs(n_filas-i)
    
        print(espacios, fila_nueva)
    
        fila_vieja = fila_nueva
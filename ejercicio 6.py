print("Tablas de multiplicar por un valor ingresado")

Numero = int(input("Ingrese un número para generar un tabla de multipliar: "))

for i in range(1,11):
    print(f'{i} X {Numero} = {i * Numero}')
    

numeros = []

valores = int(input("Ingrese el número dos: "))
numero_mayor = 0
numero_menor = 0

i = 1

while (valores > 0):
    numero = int(input("Valor Número: " + str(i) + ": "))
    numeros.append(numero)
    i = i + 1
    valores = valores - 1

numero_mayor = max(numeros)
numero_menor = min(numeros)


print("Los números ingresados son: ", numeros)
print("El número mayor es: ", numero_mayor)
print("El número menor es: ", numero_menor)

print("Número mayor de tres números")
Numero1 = int(input("Ingrese el primer número: "))
Numero2 = int(input("Ingrese el segundo número: "))
Numero3 = int(input("Ingrese el tercer número: "))

if Numero1 > Numero2 and Numero1 > Numero3:
    print("El número mayor es: ", Numero1)
elif Numero2 > Numero1 and Numero2 > Numero3:
    print("El número mayor es: ", Numero2)
elif Numero3 > Numero1 and Numero3 > Numero2:
    print("El número mayor es: ", Numero3)
else:
    print("No se puede establecer el mayor, por ser cantidades iguales")

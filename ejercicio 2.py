from math import sqrt



print("Hipotenusa de un triángulo rectángulo")
print("Ingrese los dos catetos del triángulo:")
cateto_a = float(input("Cateto a: "))
cateto_b = float(input("Cateto b: "))
hipotenusa = sqrt(cateto_a**2 + cateto_b**2)

print("La hipotenusa de los dos catetos es:", hipotenusa )

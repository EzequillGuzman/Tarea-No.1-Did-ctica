def leer_texto():
    global txt
    txt =(input("Ingrese una texto: ")).lower()
def contar_vocales():  
    vocal = ["a","e","i","o","u"]
    cont= 0

for i in vocal:
    for j in txt:
        if (i == j):
            cont+=1

            print("El número de vocales que tiene el texto es: " , cont)

leer_texto()
contar_vocales()

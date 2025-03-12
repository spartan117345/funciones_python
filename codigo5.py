import random



def sumar_lista_datos(lista):
    suma = 0
    for i in lista:
        suma = suma + i
    return suma

# entrada
# creamos una lista vacia
lisat = []
# tamaño de la lista
n = int(input("dijite el tamaño de la lista: "))

for i in range(n):
    num = random.randint(1,9)
    lisat.append(num)


# procesamiento
print("lista: ", lisat)
print("la suma es: ", sumar_lista_datos(lisat))



print("\Eso era...")
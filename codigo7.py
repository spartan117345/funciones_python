import random

def calcular_promedio_lista(lista):
    suma = 0
    for i in lista:
        suma = suma + i
        
# entrada
p = 0
m = 0
# creamos una lista vacia
lista = []
# tamaño de la lista
n = int(input("dijite el tamaño de la lista: "))

for i in range(n):
    num = random.randint(1, 9)
    lista.append(num)

# procesamiento

if lista // 2 == 0:
    p = p + 1
elif lista // 2 == 1:
    m = m + 1

else:
    print("el numero no es valido")

print("lista: ", lista)
print("la cantidad de pares es: " + str(p))
print("la cantidad de impares es: " + str(m))

# salida
print("\nEso era...")


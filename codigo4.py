
def mostrarcadena(cadena, n):
    for i in range(1, n + 1):
        print(f"{i} . {cadena}")


cadena=input("dijite la cadena a mostrar")
n = input("dijite el numero: ")

mostrarcadena(cadena, n)

print("\nEso era...")
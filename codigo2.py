print("===========================")
print("==buscar un numero oculto==")
print("===========================")

# definicion de la funcion
def buscardatosenlista(datoAbuscar, lista):
    r = False
    for i in lista:
        if 1 == datoAbuscar:
            r = True
            return r
        


# entrada 
dato = int (input("numero a buscar")) # se recibe el dato al usuario

# procesamiento


lista = (1,2,3,4,5) # se almacena una lista de datos
if buscardatosenlista(dato , lista):
    print("lo encontre")
else:
    print("no lo encontre")

# salida 
print("\neso era...")
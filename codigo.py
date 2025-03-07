print("--------------------")
print("--BUSCAR UN NUMERO--")
print("--------------------")

# entrada 
b = int(input("numero a buscar: "))#se recibe el dato del usuario

# procesamiento

a = [1,2,3,4,5] # se almacena una lista de datos

r = False # se inicia la variable r con un valor falso

for i in a:
    if i == b:
        print("lo encontre")
        r = True
if r == False:
    print("no lo encontre")

# salida 
print("\nEso era ...")

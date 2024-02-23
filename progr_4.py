lista=[]
largo = int(input("Ingrese el tamaño de la lista: "))

for i in range(largo):
    numero = int(input("Ingrese el número: "))
    lista.append(numero)
    
for numero in lista:
    print(f"{numero}-{numero**2}-{numero**3}")
    
    
    
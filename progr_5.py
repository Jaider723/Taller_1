def get_strMenor(lista):
    menor = lista[0]
    for str in lista:
        if len(str) < len(menor):
            menor = str
    return menor 

def get_strMayor(lista):
    mayor = lista[0]
    for str in lista:
        if len(str) > len(mayor):
            mayor = str
    return mayor
        
lista=[]
largo = int(input("Ingrese el tamaño de la lista: "))

for i in range(largo):
    str = input("Ingrese la cadena: ")
    lista.append(str)
    
strMenor = get_strMenor(lista)
strMayor = get_strMayor(lista)
print(f"Cadena mayor: {strMayor}")
print(f"Cadena menor: {strMenor}")
def eliminar_sin_vocales(lista):
     vocales = ["a","e","i","o","u"]
     elementos_sin_vocales = []
     for elemento in lista:
         for vocal in vocales:
             if vocal in elemento:
                elementos_sin_vocales.append(elemento)
                break
     return elementos_sin_vocales
 
lista = ["casa", "programación", "ciaf", "universidad", "ciaf", "casa", "casa","thj", "vbh", "456", "987"]

lista = list(set(lista)) #a
lista = eliminar_sin_vocales(lista) #b
lista.sort() #c

print(lista)


import random
lista = []

for i in range(15):
    valor = random.randint(1, 20)  
    lista.append(valor)

for numero in lista:
    print(f"{numero}-{numero**2}-{numero**3}")
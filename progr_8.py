lista = ["gato", "perro", "casa", "coche", "sol", "computadora", "libro", "jardín", "café", "música"]
vocales=["a","e","i","o","u"]

contador = 0
for cadena in lista:
    for letra in cadena:
        if letra not in vocales:
            contador += 1
            
print(f"La cantidad de caracteres que no son vocales es: {contador}")


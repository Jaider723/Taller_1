palabras = ["casa", "perro", "gato", "silla", "mesa", "computadora", "libro", "jardín", "auto", "ciudad", "playa"]

numero = int(input("Ingrese un número: "))
for elemento in palabras:
    if len(elemento) == numero:
        print(elemento, end=" ")
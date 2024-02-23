def es_par(cadena):
    if len(cadena)%2 == 0:
        return True
    else:
        return False

palabras = ["casa", "perro", "gato", "silla", "mesa", "computadora", "libro", "jardín", "auto", "ciudad", "playa"]

caracter = input("Ingresa un caracter: ")

for cadena in palabras:
    if caracter in cadena:
        print(cadena, end=" ")
        if es_par(cadena):
            print("es par")
        else:
            print("no es par") 
            
            
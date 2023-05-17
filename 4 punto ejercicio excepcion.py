"""
#ejercicio zerDivisorError
def division(num1,num2):
    try:
        resultado = 8/0
        print(resultado)
    except ZeroDivisionError:
        print("no se puede dividir por cero")
    
division(89,0)

print("\n")
ejercicio indexError
lista = [1, 2, 3]
try:
    elemento = lista[8]
except IndexError:
    print("Error: El índice está fuera del rango de la lista.")

print("\n")

ejercicio TypeError

try:
    resultado = "63" + 7
except TypeError:
    print("Error: No se puede concatenar una cadena de texto con un número.")

print("\n")

ejercicio ValueError
try:
    numero = int("abc")
except ValueError:
    print("Error: No se puede convertir 'abc' a un entero.")

"""
# Ejercicio 1: par o impar (if / else)
# Autor: Compañero

numero = input("Introduce un número entero: ")
try:
    numero = int(numero);
    if numero % 2 == 0:
        print(numero, "es par")
    else:
         print(numero, "es impar")
except:
    print("El valor introducido no es válido")

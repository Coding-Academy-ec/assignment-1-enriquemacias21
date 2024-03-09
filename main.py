# función que realiza la suma de dos numeros
def sumar(a, b):
    return a + b

# función que realiza el factorial de 1 numero
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Función que cuenta el número de vocales en una cadena de texto
def contar_vocales(cadena):
    vocales = "aeiouAEIOU"
    count = 0
    for char in cadena:
        if char in vocales:
            count += 1
    return count

# Función que verifica si una cadena de texto es un palíndromo
def palindromo(cadena):
    cadena = cadena.lower() # Convertir a minúsculas
    cadena = ''.join(c for c in cadena if c.isalnum()) # Quitar caracteres no alfanuméricos
    return cadena == cadena[::-1]

# Función que suma todos los elementos de una lista
def suma_lista(lista):
    return sum(lista)

if __name__ == "__main__":
    print(sumar(3, 5)) 
    print(factorial(5)) 
    print(contar_vocales("Enrique Macías")) 
    print(palindromo("casa")) 
    print(suma_lista([1, 2, 3, 4, 5])) 
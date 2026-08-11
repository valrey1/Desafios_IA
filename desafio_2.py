def es_palindromo(valor):
    valor = str(valor)

    return valor == valor[::-1]


valor = input("Ingresa una cadena o número: ")

if es_palindromo(valor):
    print("Es un palíndromo")
else:
    print("No es un palíndromo")
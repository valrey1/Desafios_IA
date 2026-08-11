resul = int(input("Elija la opcion a ejecutar 1 o 2: "))

if(resul == 1):
    print("Ejercicio: Encontrar el valor mínimo y máximo de un array")
    numeros = [15, 8, 23, 4, 42, 16, 10]
    print(f"Numeros a evaluar {numeros}")
    

    # Inicializamos mínimo y máximo con el primer elemento
    minimo = numeros[0]
    maximo = numeros[0]

    # Recorremos el array
    for numero in numeros:
        if numero < minimo:
            minimo = numero

        if numero > maximo:
            maximo = numero

    print("Valor mínimo:", minimo)
    print("Valor máximo:", maximo)

elif (resul==2):
    texto=(input("Ingrese un texto: "))
    contador = 0

    for caracter in texto:
        contador += 1

    print("La longitud de la cadena es:", contador)
else:
    print("Opción no válida")
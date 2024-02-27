def mayor_suma_consecutiva(lista):
    if len(lista) < 2:
        return "La lista debe tener al menos dos elementos"
    
    mayor_suma = lista[0] + lista[1]

    for i in range (1, len(lista)-1):
        suma_consecutiva = lista[i] + lista[i + 1]
        if suma_consecutiva > mayor_suma:
            mayor_suma = suma_consecutiva
    return mayor_suma

numeros_usuario = input("Ingrese una lista de numeros separada por espacio: ")
numeros = [int(num) for num in numeros_usuario.split()]

resultado = mayor_suma_consecutiva(numeros)
print("La mayor suma consecutiva es: ", resultado)
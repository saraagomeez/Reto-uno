# Reto uno

## PPunto uno

**Instrucción**

Cree una función que realice operaciones básicas (suma, resta, multiplicación, división) entre dos números, según la elección del usuario, la forma de entrada de la función serán los dos operandos y el carácter usado para la operación. 

**Código**
```
def realizar_operacion(num1, num2, operador):
        if operador == '+':
            resultado = num1 + num2 
        elif operador == '-':
            resultado = num1 - num2 
        elif operador == '*':
            resultado = num1 * num2 
        elif operador == '/':
            if num2 != 0:
                resultado = num1 / num2 
            else:
                return "Error: division por 0 no es permitida."
        else:
            return "Operador no valido, por favor ingrese '+', '-', '*' o '/'."
        return resultado 


if __name__ == "__main__":
    #Para solicitar entrada del usuario.
    num1 = float(input("Ingrese el primer numero: "))
    operador = input("Ingrese la operacion (+, -, *, /): ")
    num2 = float(input("Ingrese el segundo número: "))

    #Para realizar la operación.
    resultado = realizar_operacion(num1, num2, operador)

    #Para imprimir el resultado.
    print("El resultado de", num1, operador, num2, "es:", resultado)
```
**Explicación**
1. Se establecen las variables que se van a utilizar dentro de la función (num1, num2, operador).
2. Mediante la estructura de condicional **if-elif-else** se determina qué operación se va a realizar de acuerdo al operador que proporcione el usuario.
3. En caso de tener una división con denominador de 0 se arrojará un error, debido a que dicha división no es permitida.
4. En caso de no ingresar un operador válido (+, -, *, /) el programa arrojará que es un operador inválido y que deberá volverlo a intentar.
5. Se realiza un llamado de la función principal.
6. Se solicita la entrada del usuario.
7. Se realiza y se imprime el resultado de la operación.

## Punto dos

**Instrucción**

Realice una función que permita validar si una palabra es un palíndromo. Condición: No se vale hacer slicing para invertir la palabra y verificar que sea igual a la original.

**Código**
```
def palindromo(palabra):
    longitud = len(palabra)
    inicio = 0
    fin = longitud - 1

    while inicio < fin:
        if palabra[inicio] != palabra[fin]:
            return False
        inicio += 1
        fin -= 1
    return True

#Requerir entrada del usuario.
palabra_usuario = input("Ingrese una palabra o una frase sin espacios en minúsculas: ")

resultado = palindromo(palabra_usuario)

#Definir si es palíndromo o no.
if palindromo(palabra_usuario):
    print(palabra_usuario, "si es un palindromo.")
else:
    print(palabra_usuario, "no es un palindromo.")
```
**Explicación**

En esta ocasión para recorrer la palabra sin hacer slicing, la solución es recorrer la palabra desde ambos extremos al mismo tiempo.
1. Se obtiene la longitud de la palabra.
2. Se inician los indices al inicio y al final de la palabra respectivamente.
3. Se utiliza el bucle **"while"** para asegurarnos que se está comparando carácteres opuestos hasta llegar a la mitad de la palabra.
4. Se verifica que los carácteres coincidan, y se hace la confirmación mediante un **True** o un **False** dependiendo si la palabra es palíndromo o no.
5. Se imprime la solución.

## PPunto tres

**Instrucción**

Escribir una función que reciba una lista de números y devuelva solo aquellos que son primos. La función debe recibir una lista de enteros y retornar solo aquellos que sean primos.

**Código**
```
def primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True

def obtener_primos(lista):
    primos = [num for num in lista if primo(num)]
    return primos

lista_usuario = input("Ingrese una lista de numeros separados por espacios: ")
numeros = [int(num) for num in lista_usuario.split()]

resultado = obtener_primos(numeros)
print("Numeros primos: ", resultado)
```
**Explicación**

1. Se define la función "primo" y mediante el condicional **if** retorna valores de **True** o **False** dependiendo de si el número ingresado es primo o no.
2. Se define una segunda función, "obtener_primo", la cual parte de una lista inical y devuelve una segunda lista con solo núeros primos, basandose en la lista original devuelve aquellos valores para los que la función fue **True**.
3. Se pide la entrada del usuario
4. Mediante la función *split* divide la cadena que inbgresó el usuario y los devuelve como números enteros.
5. Imprime el resultado.

## PPunto cuatro

**Instrucción**

Escribir una función que reciba una lista de números enteros y devolver la mayor suma entre dos elementos consecutivos.

**Código**
```
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
```
**Explicación**
1. Se establece la longitud de la lista, si la lista tiene menos de 2 carácteres no es posible ejecutar el código.
2. Se hace la primera suma entre los dos primeros elementos de la lista ([0], [1]).
3. Se utiliza un bucle **"for"** para recorrer la lista y calcular la suma entre cada dos elementos consecutivos.
4. Se hace la comparación entre las sumas ya realizadas para saber cual es la mayor cantidad.
5. Se pide la entrada del usuario, y a la lista que se ingresa se divide y se devuelven carácteres enteros mediante la función *split*.
6. Se imprime el reesultado.

## PPunto cinco

**Instrucción**

Escribir una función que reciba una lista de cadenas y retorne únicamente aquellos elementos que tengan los mismos caracteres.

**Código**
```
abc
```
**Explicación**

1.

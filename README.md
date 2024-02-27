# Reto uno

##  Punto uno

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
2. Mediante la estructura de condicional **if-elif-else** se determina que operación se va a realizar de acuerdo al operador que proporcione el usuario.
3. En caso de tener una división con denominador de 0 se arrojará un error, debido a que dicha división no es permitida.
4. En caso de no ingresar un operador válido (+, -, *, /) el programa arrojará que es un operador inválido y que deberá volverlo a intentar.
5. Se realiza un llamado de la función principal.
6. Se solicita la entrada del usuario.
7. Se realiza y se imprime el resultado de la operación.

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
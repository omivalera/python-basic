def palindromo(palabra):
    palabra = palabra.replace(' ', '')
    palabra = palabra.lower()
    palabra_invertida = palabra[::-1]
    if palabra == palabra_invertida:
        return True
    else:
        return False
    
def main():
    palabra = input("Escribe una palbra cualquiera: ")
    es_palindromo = palindromo(palabra)
    if es_palindromo == True:
        print("Esta es una palabra palindroma")
    else:
        print("Esta es una palabra no es palindroma")


if __name__ == '__main__':
    main()
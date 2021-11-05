# import random
# import string

# def gen_password():
#     # uppr = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
#     # lowr = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#     # symb = ['!', '#', '=']
#     # numb = ['1', '2', '3', '4', '5', '6', '7', '8', '9' ,'0']
    
#     uppr = list(string.ascii_uppercase)
#     lowr = list(string.ascii_lowercase)
#     symb = list(string.ascii_punctuation)
#     numb = list(string.digts)
    
    
   
#     caract = uppr + lowr + numb
    
#     password = []
#     for i in range(15):
#         caract_random = random.choice(caract)
#         password.append(caract_random)
        
#     password = "".join(password)
#     return password


# def main():
#     password = gen_password()
#     print('Te recomiendo esta contraseña: ' + password)
    
    
#     if __name__ == '__main__':
#         main()


import random


def generar_contrasena():
    mayusculas = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    minusculas = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    simbolos = ['!', '#', '$', '&', '/', '(', ')']
    numeros = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

    caracteres = mayusculas + minusculas + simbolos + numeros

    contrasena = []

    for i in range(15):
        caracter_random = random.choice(caracteres)
        contrasena.append(caracter_random)

    contrasena = "".join(contrasena)
    return contrasena


def run():
    contrasena = generar_contrasena()
    print('Tu nueva contraseña es: ' + contrasena)


if __name__ == '__main__':
    run()
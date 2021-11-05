import random 



def main():
    numeros = random.randint(1, 100)
    numero_selec = int(input('Escoge un numero del 1 al 100: '))
    while numero_selec != numeros:
            if numero_selec < numeros:
                print('El numero es mas arriba :v')
            else:
                print('Escoge otro numero mas chico :v')
            numero_selec =int(input('Elige otro numero: '))
            print('Ganaste careverga :v')    

if __name__ == '__main__':
    main()
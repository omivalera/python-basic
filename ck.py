# Definir una función max() que tome como argumento dos números y devuelva el mayor de ellos.
x = int(input('Ingresa un numero: '))
y = int(input('Ingresa otro numero: '))

if x > y:
    print(x, sep='Este es mayor' + ' ', end='Este es mayor')
    
elif y > x: 
    print(y, sep='Este es mayor' + ' ', end='Este es mayor')
    
else:
    print('Son iguales')
    
# n1 = float(input('1) Ingresa un numero'))
# n2 = float(input('2) Ingresa un numero'))
# n3 = float(input('3) Ingresa un numero'))
# si n1 es mayor que n2 y que n1 es mayor que n3
# n1 > n2, n1 > n3
# si n2 es mayor que n1 y n2 es mayor que n3
# n2 > n1, n2 > n3
# Si n3 es mayo que n1 y n3 es mayor que n2
# n3 > n1, n3 > n2

n1 = int(input('Ingresa el primer numero: '))
n2 = int(input('Ingresa el segundo numero: '))
n3 = int(input('Ingresa el tercer numero: '))


if n1 >= n2 and n1 >= n3:
    mayor = n1
elif n2 >= n1 and n2 >= n3:
    mayor = n2
elif n3 >= n2 and n3 >= n1:
    mayor = n3
else:
    print('Los numeros son iguales')
print(f'El numero mayor es: {mayor}')
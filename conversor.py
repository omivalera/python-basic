def conversor(tipo_pesos, valor_usd):
    pesos = input("¿Cuantos " + tipo_pesos + " quieres convertir?: ")
    pesos = float(pesos)
    usd = pesos / valor_usd
    usd = round(usd, 2)
    usd = str(usd)
    print("Posees $" + usd + ", en billeticos gringos")

menu = """
💵💲Bienvenido al conversor de divisas mas basico y funcional del mundo mundial 💸🏦

Elige una opción: 

1- Soles Peruanos
2- Pesos Argentinos
3- Bolivares

Pero elige con cuidade :v: """

opcion = int(input(menu))

if opcion == 1:
    conversor("Soles", 3.98)
elif opcion == 2:
    conversor("Pesos Argentinos", 99.70) 
elif opcion == 3:
    conversor("Bolivares", 4.32)
else:
    print("no existe esa opción, tonto.")

numero = int(input("De um número :"))

if numero % 2 == 0 and numero < 100:
    print("Par e menor que 100")
elif numero % 2 == 0 and numero >= 100:
    print("Par e maior ou igual a 100")
elif numero % 2 != 0 and numero < 100:
    print("impar e menor que 100")
elif numero % 2 != 0 and numero >= 100:
    print("impar e maior ou igual a 100")
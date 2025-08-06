numero = int(input("De um número :"))

if numero % 2 == 0 :
    if numero >= 100 :
        print("par e maior ou igual a 100")
    else:
        print("par e menor que 100")
elif numero % 2 != 0 :
    if numero >= 100 :
        print("impar e maior ou igual a 100")
    else:
        print("impar e menor que 100")
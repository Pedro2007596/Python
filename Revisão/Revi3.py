velo = float(input("Quantos Kms você passou :"))
if velo >= 100 :
    print("Você estáva acima da velocidade permitida")
    if velo <= 115 :
        preco = 100
    elif velo <= 135 :
        preco = 200
    elif velo <= 180 :
        preco = 500
    elif velo >= 180 :
        preco = 1000
    print(f"Você precisa pagar {preco}")
    Paga = input("Você vai querer pagar no Débito ou no Crédito :")
    if Paga == "Débito" or Paga == "débito":
        Desc = preco * 0.1
        Valor = preco - Desc
    if Paga == "Crédito" or Paga == "crédito":
        Desc = preco * 0.15
        Valor = preco + Desc
    print(f"Você precisa pagar {Valor}")
else: print("Parábens você respeitou as leis de trânsito")
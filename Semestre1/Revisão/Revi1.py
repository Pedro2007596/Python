codMercadoria = input("Ponha o código da sua mercadoria :")
preco = float(input("O preço da sua mercadoria :"))
if codMercadoria == "00" :
    preco = preco * 10/100
if codMercadoria == "AA" :
    preco = preco * 15/100
if codMercadoria == "CC" :
    preco = preco * 35/100
print(preco)

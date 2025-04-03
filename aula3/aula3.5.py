preco = float(input("Ponha o preço da sua compra :"))
desconto = float(input("Ponha o percentual de desconto :"))

valordesconto = (desconto/100) * preco
apagar = preco - valordesconto

print(f"Você tem R$ {valordesconto}, você precisa {apagar} R$ apagar")

quantKm = float(input("Quantos Kms você deseja percorrer ? :"))
if quantKm <= 200 :
    preco = quantKm * 0.5
    print(f"Você terá que pagar {preco}")
else:
    preco2 = quantKm * 0.45
    print(f"Você terá que pagar {preco2}")
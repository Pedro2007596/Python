quantkm = float(input("Quantos Kms foram percorridos com esse carro :"))
quantDia = int(input("Quantos dias você está com esse carro :"))

valorDia = quantDia * 60
valorkm = quantkm * 0.15
valorTotal = valorDia + valorkm

print(f"Você terá que pagar R${valorTotal}")
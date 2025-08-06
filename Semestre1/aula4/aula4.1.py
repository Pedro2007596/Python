quantKm = float(input("Quantos kms por hora o carro está :"))
if quantKm > 80 :
     kmplus = quantKm - 80
     resulta = kmplus * 5
     print(f"O carro estava {kmplus} acima da média. "
           f"Você foi multado!!"
           f" você terá que pagar R${resulta}")
else:
    print("Você está na velocidade permitida")
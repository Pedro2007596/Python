print("Bem Vindo à máquina registradora, digitte o código do seu produto")
print("Código ---- preço")
print("   1 ------- 0.50 ")
print("   2 ------- 1.00 ")
print("   3 ------- 4.00 ")
print("   5 ------- 7.00 ")
print("   9 ------- 8.00 ")
print("   0 ------- enter ")
num = 0
while True :
    escolha = int(input("Digite o código do produto que você comprou : "))
    if escolha == 1:
        num = num + 0.50
        print(num)
    elif escolha == 2:
        num = num + 1.00
        print(num)
    elif escolha == 3:
        num = num + 4.00
        print(num)
    elif escolha == 5:
        num = num + 7.00
        print(num)
    elif escolha == 9:
        num = num + 8.00
        print(num)
    elif escolha == 0:
        break
    else:
        print("Código Inválido")
print(f"O valor final deu {num}")
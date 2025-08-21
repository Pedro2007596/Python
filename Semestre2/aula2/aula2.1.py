saldo = 0
extrato = []
def deposito(*args):
    global saldo
    depositar = float(input(("Quanto Você quer deposita : ")))
    saldo += depositar
    extrato.append(f'+R${depositar}')
def saque(*args):
    global saldo
    sacar = float(input(("Quanto Você quer sacar : ")))
    saldo -= sacar
    extrato.append(f'-R${sacar}')
while True:
    print(f"Bem vindo ao banco")
    print(f"Você possui R${saldo} na sua conta")
    print("Ações")
    print("1 - Depositar")
    print("2 - Sacar")
    print("3 - Extrato")
    print("4 - Sair")
    opcao = int(input("O que você gostaria de fazer : "))
    if opcao == 1:
        deposito()
    elif opcao == 2:
        saque()
    elif opcao == 3:
        print(extrato)
    elif opcao == 4:
        break
carrinho = []

def adicionar(produto):
        carrinho.append(produto)


def remover(produto):
    for i in range(len(carrinho)):
        if carrinho[i] == produto:
            carrinho.pop(i)
            break

def ver():
    for i in carrinho:
        print(i)

while True:
    print(f"Bem vindo a loja")
    print("Ações")
    print("1 - Adicionar")
    print("2 - Remover")
    print("3 - Ver")
    print("4 - Sair")
    opcao = int(input("O que você gostaria de fazer : "))
    if opcao == 1:
        produto = input("Que item você gostaria de adicionar ao seu carrinho :")
        adicionar(produto)
    elif opcao == 2:
        produto = input("Que item você gostaria de remover do seu carrinho :")
        remover(produto)
    elif opcao == 3:
        ver()
    elif opcao == 4:
        break
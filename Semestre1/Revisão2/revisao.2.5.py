print("Seja bem vindo ao jogo do número primo")
print("Eu irei pedir um número e dizer se ele é primo ou não")
while True:
    num1 = int(input("Me dê o primeiro número inteiro : "))
    if resul % 2 == 0:
        print(f"Parábens o seu resultado deu {resul} e ele é par")
    if resul % 2 != 0:
        print(f"Parábens o seu resultado deu {resul} e ele é impar")
    escolha = input("Você gostaria de continuar (S/N) :")
    if escolha == "S":
        print("Beleza vamos continuar")
    if escolha == "N":
        print("Muito obrigado por jogar")

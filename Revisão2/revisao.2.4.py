print("Seja bem vindo ao jogo de par ou impar")
print("Eu irei pedir dois número e fazer ás contas e dizer se ele é par ou impar")
while True:
    num1 = int(input("Me dê o primeiro número inteiro : "))
    num2 = int(input("Me dê o segundo número inteiro : "))
    resul = (num1 + num2)
    if resul % 2 == 0 :
        print(f"Parábens o seu resultado deu {resul} e ele é par")
    if resul % 2 != 0 :
        print(f"Parábens o seu resultado deu {resul} e ele é impar")
    escolha = input("Você gostaria de continuar (S/N) :")
    if escolha == "S":
        print("Beleza vamos continuar")
    if escolha == "N":
        print("Muito obrigado por jogar")
        break
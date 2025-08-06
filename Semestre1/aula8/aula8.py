pilha = ['Livro 1', 'Livro 2', 'Livro 3']

while True :
    print(f"Na sua fila tem {len(pilha)} pessoas")
    print(f"Pilha de livros : {pilha}")
    print("1 - Quero excluir um livro na pilha")
    print("2 - Quero colocar um livro pessoa no começo na pilha")
    print("3 - Quero acabar")
    a = input("Digite o número da ação que você quer utilizar : ")
    if a == "1":
        pilha.remove(pilha[-1])
        print(pilha)
    elif a == "2":
        x = input("Digite o neome dá pessoa que você quer adicionar : ")
        pilha.append(x)
        print(pilha)
    else:
        break
print(f"A sua pilha de livros ficou assim : {pilha}")
fila = ['Pedro', 'Maria', 'João']

while True :
    print(f"Na sua fila tem {len(fila)} pessoas")
    print(f"Fila : {fila}")
    print("1 - Quero excluir uma pessoa da fila")
    print("2 - Quero colocar uma primeira pessoa na fila")
    print("3 - Quero acabar")
    a = input("Digite o número da ação que você quer utilizar : ")
    if a == "1":
        fila.remove(fila[0])
        print(fila)
    elif a == "2":
        x = input("Digite o neome dá pessoa que você quer adicionar : ")
        fila.append(x)
        print(fila)
    else:
        break
print(f"A sua fila ficou assim : {fila}")
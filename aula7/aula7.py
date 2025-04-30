num = int(input("Digite o seu número : "))
i = 1
cont = 0
while i <= num :
    if num%i == 0:
        cont = cont + 1
        print(f"{num}/{i} = {num%i}")
    i = i + 1
if cont == 2 :
    print(f"{num} é primo")
else:
    print(f"{num} não é primo")
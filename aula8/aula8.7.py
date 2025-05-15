num = int(input("Digite o número que você quer saber se é primo : "))
pri = 0
for i in range(1,num + 1):
    if num%i == 0:
        pri += 1
if pri == 2:
    print(f"{num} é primo")
else:
    print(f"{num} não é primo")
a = int(input("Digite o primeiro número da sequencia : "))
b = int(input("Digite o último número da sequencia : "))
print(f"Você escolheu os números {a} e {b} essa é sequencia de números pares nesse intervalo")
for i in range(a,b + 1):
    if i%2 == 0:
        print(i)
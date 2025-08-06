x = 1
y = int(input("Digite o número maximo : "))

while x <= y:
    x = x + 1
    par = x % 2
    if  par == 0:
        print(x)
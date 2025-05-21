n = int(input("Digite o número de camadas que deve ter à sua àrvore :"))
for i in range(n):
    print(' '*(n-i-1)+'*'*(2*i+1))
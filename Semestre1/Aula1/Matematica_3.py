#salario = int(input("Digite seu salario:"))
#print("Seu salario é :",salario)
#cargoup = int(salario * 0.15)
#print("Você recebeu um aumento em reais de :",cargoup)
#total = salario + cargoup
#print("Seu novo salario é :",total)

a = int(input("a é igual:"))
b = int(input("b é igual:"))
c = int(input("c é igual:"))
delta = int(b**2 - 4*a*c)
x1= int((-b + delta**(1/2))/(2*a))
x2= int((-b - delta**(1/2))/(2*a))

print("X1 é igual à :",x1, "X2 é igual à :",x2)
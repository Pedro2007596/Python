print('Exercicio 1')
nota1 = (int(input('Ponha a sua primeira nota :')))
nota2 = (int(input('Ponha a sua segunda nota :')))
nota3 = (int(input('Ponha a sua terceira nota :')))

resultado = ((nota1 + nota2 + nota3)/3) > 6


print('Você passou',resultado)

print('Exercicio 2')

salario = input('Qual o seu salario :')
pagaImp = float(salario) > 1200.00
print('Você precisa pagar imposto :', pagaImp)

print('Exercicio 3')

salario = input('Qual o seu salario :')
emprestimo = float(salario) > 1000.00
print('Você precisa pegar emprestimo :', emprestimo)

print('Exercicio 3')

numeropar = int(input('Diga um número :'))

par = int(numeropar % 2)
par2 = par == 0

print('Seu número é par :', par2)

print('Exercicio 4')

numeroimpar = int(input('Diga um número :'))

impar = int(numeroimpar % 2)
impar2 = impar == 1

print('Seu número é impar :', impar2)

print('Exercicio 4')

numeroA = int(input('Diga um número :'))
numeroB = int(input('Diga um número :'))

impar1 = int(numeroA % 2)
imparA = impar1 == 1
impar2 = int(numeroB % 2)
imparB = impar2 == 1

paridade = imparA == imparB

print('Os seus números possuem a mesma paridade :', paridade)
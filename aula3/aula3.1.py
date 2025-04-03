idade = int(input("Coloque a sua idade :"))
salario = int(input("Coloque o seu salário :"))
nome = input("Ponha o seu nome :")
emprestimo = idade >= 18 and salario >= 2000
if nome == "Pedro" :
    emprestimo = True
print(emprestimo)
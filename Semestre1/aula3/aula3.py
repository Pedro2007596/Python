idade = int(input("Coloque a sua idade :"))
salario = int(input("Coloque o seu salário :"))

emprestimo = idade >= 18 and salario >= 2000
print(emprestimo)
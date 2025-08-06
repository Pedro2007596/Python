salario = float(input("Qual é o seu salário :"))
if salario > 1250.00 :
    porcenMaior = (10/100) * salario
    aumento = porcenMaior + salario
    print(f"Você recebeu um aumento de R${porcenMaior}, agora você receberá R${aumento}")
elif salario <= 1250.00 :
    porcenMenor = (15 / 100) * salario
    aumento = porcenMenor + salario
    print(f"Você recebeu um aumento de R${porcenMenor}, agora você receberá R${aumento}")
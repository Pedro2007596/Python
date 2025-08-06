nota = []
i = 1
while i <= 3:
    x = float(input("Digite a sua nota : "))
    nota.append(x)
    i+=1

soma = int(sum(nota))
qtde = int(len(nota))
media = soma/qtde
print(f"Às notas são {nota} e a média delas é {media}")
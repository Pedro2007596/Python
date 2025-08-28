lin = 3
col = 4
matriz = []
for j in range(lin):
    linha = []
    for i in range(col):
        linha.append(int(input('Digite um valor : ')))
    matriz.append(linha)
print(matriz)

qntdedelinhas = len(matriz)
qntdedecolunas = len(matriz[0])

print(qntdedelinhas)
print(qntdedecolunas)
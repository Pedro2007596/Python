lin = int(input("Digite o número de linhas que essa matrix deve ter : "))
col = int(input("Digite o número de colunas que essa matrix deve ter : "))
matriz = []
for j in range(lin):
    linha = []
    for i in range(col):
        linha.append(int(0))
    matriz.append(linha)
print(matriz)

lin = int(input("Digite o número de linhas que essa matrix deve ter : "))
col = int(input("Digite o número de colunas que essa matrix deve ter : "))
matriz = []
for j in range(lin):
    linha = []
    for i in range(col):
        linha.append(int( i + j * col)+ 1)
    matriz.append(linha)
print(matriz)
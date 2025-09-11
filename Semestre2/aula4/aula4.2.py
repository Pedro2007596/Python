d = {}

while True:
    print(d)
    op = input('Digite 1 para adicionar no dicionário; 2 para consultar; 3 sair: ')

    if op == '1':
        chave = input('Digite a chave')
        valor = input('Digite o valor')
        d[chave] = valor
    elif op == '2':
        chave = input('Digite a chave para consulta: ')
        print(d.get(chave))
    elif op == '3':
        break
    else:
        print('Comando inválido!')

# Faça um programa que permita ao usuário adicionar pares chave e valor em uma
# estrutura do tipo dicionario
# permita tbm o usuário escolher uma chave para ver o valor
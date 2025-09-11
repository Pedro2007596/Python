a = {
    'lat' : 1.98,
    'long': 2.102,
    10: 'Valor',
    3.42: [1,4,6],
    ('x','y'): [1,2]
}
print(a)

def valor(d, c):
    if c in d:
        return d[c]
    return print('None')

pessoa = {
    'nome' : 'Pedro',
    'idade': '18',
    'peso': '66',
    'altura': 1.75,
    'trabalho': {1:'Fiap',2:'innovation'}
}

pessoa['nome'] = 'João'
print(pessoa)
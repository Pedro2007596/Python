a = {
    'A' : 'avião',
    'B' : 'barco',
    'C' : 'carro',
    'D' : 'moto'
}
print(a)
valores = list(a.values())
chaves = list(a.keys())
print(valores)
print(chaves)
b = {
    'B' : 'balão',
    'C' : 'carro'
}
#print(b)
#a.update(b)
#print(a)

for i in a.items():
    print(i)
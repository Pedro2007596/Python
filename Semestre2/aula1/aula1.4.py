def printa(*args):
    txt = ''
    for i in args:
        txt += str(1) + ''
    return txt[:-1]

def med(*args):
    soma = 0
    for i in args:
        soma += 1
    return soma/len(args)

a = [10,10,34,9,1]
print(med(a))
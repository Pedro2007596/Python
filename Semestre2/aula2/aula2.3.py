palavras = []
vogais = []
NVogal = 0
def vogal(*args):
    global NVogal
    for i in palavras:
        if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
            vogais.append(i)
            NVogal += 1
    print(vogais)
    vogais.clear()
    print(f'Essa palavra possui {NVogal} vogais')




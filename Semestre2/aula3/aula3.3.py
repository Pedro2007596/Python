l = [i**2 for i in range(1,11)]
print(l)

l1 = [i for i in range(1,21) if i % 2 == 0]
print(l1)

palavras = ['Python', 'List', 'comprehension', 'exercícios']
l3 = [len(i) for i in palavras]
print(l3)

celsius = [0, 10, 20, 30, 40]
l4 = [i*9/5 +32 for i in celsius]
print(l4)

l5 = ['Fizz' if i % 3 == 0 else i for i in range(1,21)]
print(l5)

frutas = ['Maçã', 'Banana', 'Uva', 'Morango', 'abacaxi']
l6 = [i for i in frutas if len(i) > 5]
print(l6)


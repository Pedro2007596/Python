import math

l1 = []
for i in range(10):
    l1.append(2*i)
print(l1)

l3 = [0 for i in range(1000)]
print(l3)

notas = [10, 8, 7, 4, 6]
l4 = [i for i in notas if i >= 6]
print(l4)

l5 = [i for i in range(0,100) if i % 2 != 0]
print(l5)

angulo = [3.14, 0, 1.72, 2*3.14]
senos = [math.mu(i) for i in angulo]
print(senos)
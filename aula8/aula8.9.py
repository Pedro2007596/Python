num = int(input("Digite o número : "))

l1 = []
l2 = []
for i in range(num+1):
    for a in range(0,num+1):
        for b in range(0,num+1):
            if a + b == num:
                l1.append(a)
                l2.append(b)
                print(f"{a} + {b} = {num}")

print(l1)
print(l2)
a = int(input("Digite o valor de a :"))
b = int(input("Digite o valor de b :"))
c = int(input("Digite o valor de c :"))

if a > b > c :
    print(f"o maior numero é {c} e o menor é {a}")
elif b > a > c :
    print(f"o maior numero é {c} e o menor é {b}")
elif c > a > b :
    print(f"o maior numero é {b} e o menor é {c}")
elif a > c > b :
    print(f"o maior numero é {b} e o menor é {a}")
elif c > b > a:
    print(f"o maior numero é {a} e o menor é {c}")
elif b > c > a:
    print(f"o maior numero é {a} e o menor é {b}")
KW = float(input("Quantos KWh foram consumidas ? Digite aqui :"))
tipo = input("Que tipo de lugar você está pagando? R para residencia I para industrias e para Comércios Digite aqui :")

if KW <= 500 and tipo == "R" or "r":
    Total = KW * 0.4
else: Total = KW * 0.65

if KW <= 1000 and tipo == "C" or "c":
    Total = KW * 0.55
else: Total = KW * 0.6
if KW <= 5000 and tipo == "I" or "i":
    Total = KW * 0.55
else: Total = KW * 0.6

print(Total)
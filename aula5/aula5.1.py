cpf = input("Digite o seu cpf : ")

cal1 = int(cpf[0])*10 + int(cpf[1])*9 + int(cpf[2])*8 + int(cpf[3])*7 + int(cpf[4])*6
cal1 = cal1 + int(cpf[5])*5 + int(cpf[6])*4 + int(cpf[7])*3 + int(cpf[8])*2
rest1 = cal1 % 11
if 11 - rest1 < 10:
    dig1 = 11 - rest1
else:
    dig1 = 0

cal2 = int(cpf[0]) * 11 + int(cpf[1]) * 10 + int(cpf[2]) * 9 + int(cpf[3]) * 8 + int(cpf[4]) * 7
cal2 = cal2 + int(cpf[5]) * 6 + int(cpf[6]) * 5 + int(cpf[7]) * 4 + int(cpf[8]) * 3 + dig1*2
rest2 = cal2 % 11
if 11 - rest2 < 10:
    dig2 = 11 - rest2
else:
    dig2 = 0

if dig1 == int(cpf[9]) and dig2 == int(cpf[10]):
    print(f'O cpf:{cpf} é válido')
else:
    print(f'O cpf:{cpf} é inválido. Os digitos verificadores são: {dig1}{dig2}')

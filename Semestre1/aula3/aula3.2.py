cliente = input("Ponha o seu estado :")
atividade = input("Você é um cliente ativo Ativo = 0, Inativo = 1 :")

estado = cliente == "São Paulo" or cliente == "Minad Gerais" or cliente == "SP" or cliente == "MG" or cliente == "Sp" or cliente == "Mg" and atividade == "1"
print("Você vai receber um voucher :", estado)
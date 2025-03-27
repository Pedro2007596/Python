seg = 100000
minu = seg // 60
segf = seg % 60

hora = minu // 60
minuf = minu % 60

dia = hora // 24
horaf = hora % 24

print(dia)
print(horaf)
print(minuf)
print(segf)

dia = 1
horas = 3
minu = 46
seg = 40

segDia = dia * 86400
segHoras = horas * 3600
segMinu = minu * 60
segTotal = segDia + segHoras + segMinu + seg
print('segundos totais', segTotal)
text = "Hoje-tem-aula-de-python"
txt1 = text[::2]
txt2 = text[1::2]
i = 0
txt = ''
while i < len(txt2):
    txt = txt + txt1[i] + txt2[i]
    i += 1
if len(txt1 + txt2) % 2 == 1:
    txt = txt + txt1[i]
print(txt)

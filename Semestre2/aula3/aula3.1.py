a = lambda x,y,z: x + y + z

print(a(x = 3, y=2, z=1))

b = lambda reverse : reverse[::-1]

print(b('pedro'))

b = lambda palindromo :'Verdade' if palindromo == palindromo[::-1] else 'Falso'

print(b('ana'))
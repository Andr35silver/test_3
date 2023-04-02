palabras = 0
x = dict()
line = input('Ingrese un texto: ')

for a in line :
    palabras = a.rstrip()
    
    for w in palabras:
        x[w] = x.get(w,0) + 1
print(x)
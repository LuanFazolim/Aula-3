numeros=[]
imp=[]
par=[]
for set in range(1,8):
    num=int(input(f'Digite o {set}o valor: '))
    if num%2 == 0:
        par.append(num)
    else:
        imp.append(num)
numeros.append(imp)
numeros.append(par)

print('Pares: ',end='')
print(sorted(numeros[1]))
print('Impares: ',end='')
print(sorted(numeros[0]))

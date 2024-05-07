lista=[]
cont=0
fcont=0
maior=[]
maior.append(0)
ff=1
r=1
par=[]
m=('''    1     2     3
1 [ ? ] [ ? ] [ ? ]
2 [ ? ] [ ? ] [ ? ]
3 [ ? ] [ ? ] [ ? ]''')
for q in range(1,10):
    if cont == 0:
        print(m)
    while cont <= 2:
        n=int(input(f'Digite um valor para [1, {fcont+1}]: '))
        if n%2 == 0:
            par.append(n)
        lista.append(n)
        cont += 1
        fcont+=1
    fcont=0
    while cont <= 5:
        n=int(input(f'Digite um valor para [2, {fcont+1}]: '))
        if n%2 == 0:
            par.append(n)
        if n > maior[0]:
            maior.clear()
            maior.append(n)
        lista.append(n)
        cont += 1
        fcont+=1

    fcont=0
    while cont <= 8:
        n=int(input(f'Digite um valor para [3, {fcont+1}]: '))
        if n%2 == 0:
            par.append(n)
        lista.append(n)
        cont += 1
        fcont+=1
print(20*'-=')
print(('''    1     2     3'''))
for e in range (0,9):
    if ff == 1:
        print(r,end=' ')
        r+=1
    print(f'[ {lista[e]} ]',end=' ')
    if ff == 3:
        print()
        ff=0
    ff+=1
print(20*'-=')
l=len(par)
soma=0
for t in range(0,l):
    soma+=par[t]

sol=lista[2]+lista[5]+lista[8]


print(f'A soma dos valores pares e {soma}')
print(f'A soma dos valores da terceira coluna e {sol}')
print(f'O maior valor da segunda linha e {maior[0]}')
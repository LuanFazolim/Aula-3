lista=[]
cont=0
fcont=0
ff=1
r=1
m=('''    1     2     3
1 [ ? ] [ ? ] [ ? ]
2 [ ? ] [ ? ] [ ? ]
3 [ ? ] [ ? ] [ ? ]''')
for q in range(1,10):
    if cont == 0:
        print(m)
    while cont <= 2:
        n=int(input(f'Digite um valor para [1, {fcont+1}]: '))
        lista.append(n)
        cont += 1
        fcont+=1
    fcont=0
    while cont <= 5:
        n=int(input(f'Digite um valor para [2, {fcont+1}]: '))
        lista.append(n)
        cont += 1
        fcont+=1

    fcont=0
    while cont <= 8:
        n=int(input(f'Digite um valor para [3, {fcont+1}]: '))
        lista.append(n)
        cont += 1
        fcont+=1
print()
print(('''     1       2       3'''))
for e in range (0,9):
    if ff == 1:
        print(r,end=' ')
        r+=1
    print(f'[ {lista[e]:^3} ]',end=' ')
    if ff == 3:
        print()
        ff=0
    ff+=1




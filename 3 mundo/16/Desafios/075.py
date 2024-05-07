n1=int(input('Digite um numero: '))
n2=int(input('Digite outro numero: '))
n3=int(input('Digite mais um numero: '))
n4=int(input('Digite ao ultimo numero: '))
tup=n1,n2,n3,n4
co=0
print('Voce digitou os valores:',end=' ')
for ger in range(0,4):

    print(tup[ger],end=' ')
print()
if 9 in tup:
    n=tup.count(9)
    if n == 0:
        print('O valor 9 apareceu 1 vez')

    if n >=1:
        print(f'O valor 9 apareceu {n} vezes')
if not 9 in tup :
    print(f'O valor 9 nao apareceu nenhuma vez!')


if 3 in tup:
    t=tup.index(3)
    if t == 0:
        print('O valor 3 apareceu na 1º posiçao')


    if t >= 1:
        print(f'O valor 3 apareceu na {t+1}º posiçao')

if not 3 in tup:
    print(f'O valor 3 nao apareceu em nenhuma posiçao!')


if 2 in tup or 4 in tup  or 6 in tup  or 8 in tup  or 10 in tup:
    print('Os numeros pares sao:',end='\033[33m ')
    if tup[0]%2==0:
        print(tup[0],end=' ')

    if tup[1] % 2 == 0:
        print(tup[1], end=' ')

    if tup[2] % 2 == 0:
        print(tup[2], end=' ')

    if tup[3] % 2 == 0:
        print(tup[3], end=' ')
else:
    print('Nao temos numeros pares')

print()
print()
#==================================================================================================================
num=(int(input('\033[m1 valor: ')),
     int(input('2 valor: ')),
     int(input('3 valor: ')),
     int(input('4 valor: ')))
print(f'Voce digitou os valores {num} ')
print(f'O valor 9 apareceu {num.count(9)} vezes')



if 3 in num:
    print(f'O valor 3 apareceu na {num.index(3)+1}º posiçao')
else:
    print(f'O valor 3 nao apareceu em nenhuma posiçao!')




print('Os valores pares sao ', end='')
for we in num:
    if we%2 ==0:
        print(we,end=' ')



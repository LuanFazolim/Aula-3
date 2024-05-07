#TUPLAS SAO IMUTAVEIS
p1=str(input('Digite o nome de uma pessoa: '))
p2=str(input('Digite o nome de outra pessoa: '))
p3=str(input('Digite o nome de outra pessoa: '))
p4=str(input('Digite o nome de outra pessoa: '))
n=int(input('Posiçao: '))
n-=1
pt=p1,p2,p3,p4.capitalize()
print()
print(pt[n])
print(60*'=-')
#======================================================================================================================
print()
print(pt)
print()
print("Para tirar os ' e os )")
c=1
print()
for pessoas in pt:
    print(f'Pessoa {c} = {pessoas}')
    c+=1
#Ou
print()
print('OU')
print()

for pessoas2 in range(0,len(pt)):
    print(pt[pessoas2])

#Ou
print()
print('OU')
print()

for pos,pessoas in enumerate(pt):
    print(f'{pessoas} ! Esta na posiçao {pos+1}')
print()

#===========================================================================================================================
print(60*'=-')
print('Ordem')
print(sorted(pt))
print()

#===========================================================================================================================
print(60*'=-')
print('Junçao')
n1=int(input('Digite um numero: '))
n2=int(input('Digite o segundo numero: '))
print()
n3=int(input('Digite o outro numero: '))
n4=int(input('Digite o ultimo numero: '))
a=n1,n2
b=n3,n4
c=a+b
print(f'\033[33m{a}\033[m + \033[34m{b}\033[m = {c}')
print(f'Ao todo temos {len(c)} numeros')
print(f'O numero primeiro 5 aparece {c.count(5)} vezes')
i=c.index(5)
print(f'E o numero 5 esta na {i+1} posiçao')
if c.count(5) >1:

    print(f'E o outro esta na posiçao {i+2}')
print()

print()

#===========================================================================================================================
print(60*'=-')
print('DELETE ')
print('Use o comando "del(\033[37mVARIAVEL\033[m") para apagar uma variavel')
print(f'Ao apagar a variavel "pt = {pt} "\n\033[47;1;31m O comando finaliza!!\033[m')
del(pt)
print(pt)

#===========================================================================================================================
print(60*'=-')




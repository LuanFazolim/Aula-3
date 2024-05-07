lista=list()
for c in range(0,5):
    lista.append(int(input('Digite um valor: ')))
while True :
    print(f'\033[1;33m{lista}\033[m')


    addous=str(input('ADD ou SUBSTITUIR ou REMOVER (Se digitar "n" o programa acaba): ')).lower().strip()[0]
    if addous in 'n':
        break
    if addous in 'r':
        remo=int(input('Em que posiçao esta o numero que deseja remover: '))
        if remo not in lista:
            print('Nao removemos nenhum ')
        else:
            print(f'Voce removeu o numero {lista[remo-1:remo]}')
            lista.pop(remo-1)


    if addous in 's':
        po = int(input('Subistituir a posiçao: '))
        num = int(input('para o numero: '))
        if 0<po<10:
            lista[po-1]=num



    elif addous in 'a':
        num = int(input('numero: '))
        po = str(input('entre a posiçao: '))[0]
        po=int(po)

        if po >10:
            lista.append(num)
        elif 0<po<10:
            lista.insert(po,num)
print()

for v in lista:
   print(f' \033[1;33m{v}\033[m',end='')

lista.sort()
print('\nOrdem \033[34mcrecente\033[m:\n',lista)
lista.sort(reverse=True)
print('Ordem \033[31mdecrecente\033[m:\n',lista)


#============================================================================================================

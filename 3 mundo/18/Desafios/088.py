from random import randint
lista=[]
corda=[]

print(20*'=','MEGA SENA',20*'=')
nu=int(input('Quantos jogos: '))
for re in range(0,nu):
    for meg in range(0,6):
        ale=randint(1,60)
        for repe in range(0,meg):
            while ale == corda[repe]:
                ale = randint(1, 60)
        corda.append(ale)
        corda=sorted(corda)
    lista.append(corda[:])
    corda.clear()
print('-=-=-=',f'Sorteando {nu} Jogos','-=-=-=')

for ww in range(0,nu):
    print(f'Jogo {ww+1}: {lista[ww]}')
print('-=-=-=-=-=',f'< BOA SORTE! >','-=-=-=-=-=')
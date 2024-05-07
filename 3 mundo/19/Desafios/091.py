from random import choice
from time import sleep
from operator import itemgetter
dado={}
x = 1,2,3,4,5,6

for so in range(1,5):
    c = choice(x)
    dado[f'jogador{so}']=c

print(20*'=','Valores Sorteados',20*'=')
print()
rank={}
for k,i in dado.items():
    print(20*' ',f'{k} tirou {i}')
    sleep(0.5)
rank=sorted(dado.items(),key=itemgetter(1),reverse=True)
print()
print()
print(20*'=','Ranking dos Jogadores',20*'=')
for d ,o in enumerate(rank):
   print(20*' ',f'{d+1}o. Lugar: {o[0]} com {o[1]}.')
   sleep(0.5)
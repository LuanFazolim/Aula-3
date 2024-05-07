dc={}
gols=[]
dc['nome']=str(input('Nome: ')).capitalize()
total=0
part=int(input(f'Quantas partidas {dc["nome"]} jogou: '))
print()

for ss in range(1,part+1):
    gols.append(int(input(f'Quantos gols na {ss}o. partida: ')))
    total+=gols[ss-1]

dc['gols']=gols[:]
dc['total']=total

print()
print(dc)
print('-='*50)
print(f'O campo "nome" tem o valor de {dc["nome"]} ')
print(f'O campo "gols" tem o valor de {dc["gols"]} ')
print(f'O campo "total" tem o valor de {dc["total"]} ')
print('-='*50)
print(f'O jogador {dc["nome"]} jogou {part} partidas.')

for rr in range(1,part+1):
    print(7*' ',f'=> Na partida {rr}, fez {gols[rr-1]} gols.')
print(f'Foi um total de {dc["total"]} gols.')
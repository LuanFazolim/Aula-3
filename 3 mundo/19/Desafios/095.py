dc={}
joga=[]
gols=[]
cont=0
total=0
while True:
    cont+=1
    print(40 * '-')
    dc['nome']=str(input('Nome do Jogador: ')).capitalize()
    part=int(input(f'Quantas partidas {dc["nome"]} jogou?: '))
    print()
    for p in range(1,part+1):
        gols.append(int(input(f'Quantos gol na {p}o. partida? ')))
        total+=gols[p-1]
    dc['gols']=gols[:]
    gols.clear()
    dc['total']=total
    joga.append(dc.copy())
    total=0
    print(40 * '-')


    sn=str(input('Quer continuar? [S/N] ')).lower()
    print()
    if sn == 'n':
         break
print(joga)
print(40*'-=')
print()
print('cod nome',15*' ','gols',17*' ','total')
print(70*'-')
for w in range(1,cont+1):
    print(f' {w} {joga[w-1]["nome"]:<20}',end='')
    print(f'{joga[w-1]["gols"]}',end='')
    print(f'{joga[w-1]["total"]:>15}')

print(70*'-')

while True:
    print(70 * '-')
    dado=int(input('Mostrar dados de qual jogador?: '))
    print()
    if dado == '999':
        print('<< VOLTE SEMPRE >>')
        break
    elif dado > cont:
        print(f'ERRO! nao existe jogador na {dado}o. pocisao! tente novamente')
    else:
        print(f'-- LEVANTAMENTO DO JOGADOR {joga[dado-1]["nome"]} :')
        for t in range(0,len(joga[dado-1]["gols"])):
            print(f'    No {t+1}o. jogo fez {joga[dado-1]["gols"][t]} gols.')






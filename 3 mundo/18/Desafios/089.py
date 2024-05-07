fod=0
dados=[]
liga=[]
nota=[]

while True:
    liga.clear()
    nota.clear()
    fod+=1
    print('----------------------------')
    print(f'{fod})')
    nome=input('Nome: ').capitalize()
    no1=float(input('Nota 1: '))
    no2 = float(input('Nota 2: '))
    nota.append(no1)
    nota.append(no2)
    liga.append(nome)
    liga.append(nota[:])
    liga.append((no1+no2)/2)
    dados.append(liga[:])

    print('----------------------------')
    sn=input('Continuar? [S/N] ').lower()
    print()
    if sn == 'n':
        break
print(40*'-=')
print('No. NOME',20*' ','MEDIA')
print(40*'-')
for sl in range(1,fod+1):
    print(f' {sl}   {dados[sl-1][0]:<25} {dados[sl-1][2]:.1f}' )
print(45*'-')
while True:
    al=int(input('Mostrar notas de qual aluno? \033[37m(00 acaba)\033[m: '))
    if al == 00:
        break
    print(f'As notas de {dados[al-1][0]} sao {dados[al-1][1]}')
    print()


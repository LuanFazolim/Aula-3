dados=[]
dc={}
mul=[]
aci=[]
cont=0
idade=0
while True:

    cont+=1
    print(40*'-')
    dc['nome']=str(input('Nome: ')).capitalize()
    dc['sexo'] = str(input('Sexo: [M/F] ')).upper()
    if dc['sexo'] == 'F':
        mul.append(dc['nome'])
    dc['idade'] = int(input('Idade: '))
    idade+=dc['idade']
    print(40 * '-')

    dados.append(dc.copy())
    dc.clear()


    sn=input('Quer continuar? [S/N] ').lower()
    if sn == 'n':
        break

    print()

media=float(idade/cont)

print()
print(50*'-=')
print(f'- O grupo tem {cont} pessoas.')
print(f'- A media de idade e de {media:.2f} anos.')
print('- As mulheres cadastradas foram: ',end='')
for m in mul:
    print(f'[ {m} ]',end=' ')
print()
print('- Listas das pessoas que estao acima da media:')
print()
for r in range(0,cont):
    if dados[r]['idade'] > media:
        print(f'Nome = {dados[r]["nome"]}; sexo = {dados[r]["sexo"]}; idade = {dados[r]["idade"]}')
        print()
print('<< ENCERRADO >>')
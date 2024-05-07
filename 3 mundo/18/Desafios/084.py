dados=[]
ligacao=[]
maior=[]
mnome=[]
peq=[]
pnome=[]
cont=0
while True:
    print('---------------------')

    nome=str(input('Nome: '))
    ligacao.append(nome)
    peso=float(input('Peso: '))
    #maior
    if cont == 0:
        maior.append(peso)
        mnome.append(nome)
    elif peso > maior[0]:
        maior.clear()
        mnome.clear()
        maior.append(peso)
        mnome.append(nome)
    elif peso == maior[0]:
        mnome.append(nome)

    #menor
    if cont == 0:
        peq.append(peso)
        pnome.append(nome)

    elif peso < peq[0]:
        peq.clear()
        pnome.clear()
        peq.append(peso)
        pnome.append(nome)
    elif peso == peq[0]:
        pnome.append(nome)




    ligacao.append(peso)
    dados.append(ligacao[:])
    ligacao.clear()

    print('---------------------')

    cont+=1

    sn=str(input('Continuar [S/N] ')).lower()
    if sn == 'n':
        break
    print()
maior.append(mnome[:])
peq.append(pnome[:])

print(f'{cont} pessoas ')

#grande
print(f'Mais pesado {maior[0]}Kg ',end=':')
l=len(mnome)
for www in range(0,l):
    print(f'[{mnome[www]}]',end=' ')
print()


#pequeno
print(f'Menos pesado {peq[0]}Kg ',end=':')
le=len(pnome)
for ww in range(0,le):
    print(f'[{pnome[ww]}]',end=' ')

print()





lista=list()
y='y'
while not y =='n':

    pe=int(input('Digite um valor: '))
    if pe in lista:
        print('\033[1;47;31mValor duplicado!\033[m nao vou colocar')
    else:
        lista.append(pe)
        sorted(lista)

    y=str(input('Quer continuar [\033[32mY\033[m/\033[31mN\033[m] ')).lower()
    print(40*'-')
print('Voce digitou os valores: ',end='\033[33m')
lista.sort()
for c in lista:
    print(f'{c}',end=' ')


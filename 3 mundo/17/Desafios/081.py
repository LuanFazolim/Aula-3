lista=list()
con=0
y='y'
while not y == 'n':
    pe=lista.append(int(input('Digite um valor: ')))
    con+=1
    y=str(input('Quer continuar [\033[32mY\033[m/\033[31mN\033[m] ')).lower()
print(f'Voce digitos \033[35m{con}\033[m elementos')
lista.sort(reverse=True)
print(f'Os valores em ordem decrecente sao \033[33m{lista}\033[m')

if 5 in lista:
    print('O valor \033[34m5 faz\033[m parte da lista!!')
else:
    print('O valor \033[31m5 nao\033[m faz parte da lista!!')
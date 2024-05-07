lista=list()
for la in range(0,5):
    lista.append(int(input('Digite um valor: ')))
print('voce digitou os valores:',end=' ')
for c in lista:
    print(f'\033[34m{c}\033[m',end=' ')
print()
m=max(lista)
p=min(lista)

print(f'O \033[34mmaior\033[m valor e \033[32m{m}\033[m',end=' ')

print(f'que esta nas posiçoes',end=' ')
for i,v in enumerate(lista):
    if v == m:
        print(f'\033[33m{i+1}\033[m...',end='')

print(f'\nO \033[31mmenor\033[m valor e \033[32m{p}\033[m',end=' ')
print(f'que esta nas posiçoes',end=' ')
for i,v in enumerate(lista):
    if v == p:
        print(f'\033[33m{i+1}\033[m...',end='')

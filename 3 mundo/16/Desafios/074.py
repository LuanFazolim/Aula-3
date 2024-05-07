
from random import choice
uad=(1,2,3,4,5,6,7,8,9,10)
print('Os valores foram: ',end='')
a=0,
for rep in range(0,5):
    c=choice(uad)
    a+=uad[c-1:c]
    print(f'\033[1;33m{c}\033[m',end=' ')
s=sorted(a)
print(f'\nO maior valor sorteado foi \033[34m{s[5]}\033[m')
print(f'O menor valor sorteado foi \033[31m{s[1]}')

#+===============================================================================
from random import randint
uad=(randint(1,10)),(randint(1,10)),(randint(1,10)),(randint(1,10)),(randint(1,10)),
print('Os valores foram: ',end='')
for rep in uad:

    print(f'\033[1;33m{rep}\033[m',end=' ')
print(f'\nO maior valor sorteado foi \033[34m{max(uad)}\033[m')
print(f'O menor valor sorteado foi \033[31m{min(uad)}')


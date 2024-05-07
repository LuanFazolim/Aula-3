
lista=list()
par=list()
impar=list()
y='y'
con=1
while not y == 'n':
    pe = int(input('Digite um valor: '))
    if pe %2 ==0:
        par.append(pe)
    else:
        impar.append(pe)

    lista.append(pe)

    y = str(input('Quer continuar [\033[32mY\033[m/\033[31mN\033[m] ')).lower()
    con+=1
print(30*'-==')
print()
print(f'A lista completa e\033[33m {lista}\033[m')

print(f'Os pares sao:\033[34m {par}\033[m')
print(f'Os impares sao: \033[35m{impar}\033[m')

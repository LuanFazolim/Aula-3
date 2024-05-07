galera=list()
nome=list()


for rr in range(1,4):
    Nome=nome.append(input(f'\033[1;35m{rr}.\033[m Digite um nome: '))
    idade=nome.append(int(input('    \033[36mIdade:\033[m ')))
    galera.append(nome[:])
    nome.clear()
print(galera)
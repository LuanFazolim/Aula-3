ex=input('Digite sua expressao: ')
con=ex.count('(')
con2=ex.count(')')
if con == con2:
    print('A expressao e \033[32mvalida!!!')
else:
    print('A expressao e \033[31mivalida!!!')


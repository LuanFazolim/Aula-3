dados={}
dados['nome']=str(input('Seu nome: ')).capitalize()
dados['media']=float(input(f'Media de {dados["nome"]}: '))
print(40*'-')
print(f'Nome e igual a {dados["nome"]}')
print(f'Media e igual a {dados["media"]}')
print('Situacao igual a',end=' ')
if 5 < dados['media'] >= 7:
    print('\033[1;32mAPROVADO\033[m')

elif dados['media'] >=5:
    print('\033[1;33mRECUPERACAO\033[m')
else:
    print('\033[1;31mREPROVADO\033[m')


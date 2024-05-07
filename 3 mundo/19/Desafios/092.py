dc={}

dc['nome']=str(input('Nome: ')).capitalize()
idade=int(input('Ano de Nacimento: '))
dc['idade']=2023-idade
dc['ctps']=int(input('Carteira de Trabalho (0 nao tem): '))
if dc['ctps']== 0:
    print()
    print(f'Seu nome e {dc["nome"]}')
    print(f'Sua idade e {dc["idade"]}')
    print('Voce nao tem carteira de trabalho')

else:
    dc['cont'] = int(input('Ano de contratacao: '))
    apo=(dc['cont']-idade)+35
    dc['apo']=apo
    dc['sala'] = int(input('Seu salario R$: '))
    print(40*'-=')
    print()

    print(f'Seu nome e {dc["nome"]}')
    print(f'Sua idade e {dc["idade"]}')
    print(f'Sua carteira de trabalho e: {dc["ctps"]}')
    print(f'Sua contratacao foi em {dc["cont"]}')
    print(f'Seu Salario e de {dc["sala"]} R$')
    print(f'Sua aposentadoria sera ou foi com {dc["apo"]} anos')


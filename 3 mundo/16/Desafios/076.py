print(50*'\033[1m-\033[m')
print('               LISTAGEM DE PREÇO')
print(50*'\033[1m-\033[m')
loja=0,'Lapis',1.75,'Borracha',2.00,'Caderno',15.90,'Estojo',25.00,'Transferidor',4.20,'Compasso',9.99,'mochila',120.32,'Caneta',22.30,'Livro',34.90
rs='..............................R$'
for re in range(1,19,2):
    print(f'{loja[re]:.<30}'.strip(),end='')
    print(f'R$ {loja[re+1]}')

print(50*'\033[1m-\033[m')
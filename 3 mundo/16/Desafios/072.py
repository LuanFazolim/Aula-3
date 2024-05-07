pe=int(input('Escreva um numero entre 0 e 20: '))

cont=0
while pe < 0 or pe>20:
    cont+=1
    pe=int(input('\033[1;31mBURRO!!\033[m ESCREVA UM NUMERO ENTRE 0 E 20: '))
    if cont == 2:
        pe = 21
        print('VOCE E MUITO \033[1;31mBURRO!!!\033[m ')
        break
dzav='zero','um','dois','tres','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','quatorze','quinze','dezesseis','dezesete','dezoito','dezenove','vinte',''



r1 = (dzav[pe])
r = r1.upper()

print(f'Voce digitou o numero \033[34m{r}')

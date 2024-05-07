palavras1='amor','coco','dormir','jogar','livro','castor','lousa','arara','comer','comemorar'


for re in range(0,10):
    palavras=str(palavras1[re])

    a = ''
    e = ''
    i = ''
    o = ''
    u = ''

    if 'a' in palavras:
        a=palavras.count('a')

        if a >=1:
            a=a* ' a'



    if 'e' in palavras:
        e = palavras.count('e')
        if e >=1:
            e=e* ' e'

    if 'i' in palavras:
        i = palavras.count('i')
        if i >=1:
            i=i* ' i'
    if 'o' in palavras:
        o = palavras.count('o')
        if o >=1:
            o=o* ' o'
    if 'u' in palavras:
        u = palavras.count('u')
        if u >=1:
            u=u* ' u'
    print(f'Na palavra \033[1;35m{palavras.upper()}\033[m temos as vogais \033[31m{a}\033[32m{e}\033[33m{i}\033[34m{o}\033[35m{u}\033[m')







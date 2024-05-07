num= list()
for re in range(0,5):
    pe=int(input('Digite um valor: '))
    if re == 0:
        print('Primeiro numero...')
        num.append(pe)
    elif pe > num [-1]:
        print('Ultimo numero...')
        num.append(pe)

    else:
        pos = 0
        while pos < len(num):
            if pe <= num[pos]:
                num.insert(pos,pe)
                print(f'add na {pos+1} posiçao')
                break
            pos+=1
print('-='*30)
print(f'Os valores foram \033[33m{num}')




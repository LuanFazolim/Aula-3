def e():
    print()
def tr():
    print(30*'-')

print('ola')


e()
print('como estas')
e()

#---------------------------------------------------------
print('-='*30)

e()




def titulo(txt):
    tr()
    print(7*' ',txt)
    tr()


while True:
    d=input('Escreva algo: ')
    if d == '00':
        break


    titulo(d)
    e()

#------------------------------------------------------------------
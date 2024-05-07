

def lin(txt):
    print('~~'+len(txt)*'~'+'~~')
    print('  '+txt)
    print('~~' + len(txt) * '~' + '~~')


while True:
    p=input('Digite algo: ')
    if p == '000':
        break

    lin(p)
    print()
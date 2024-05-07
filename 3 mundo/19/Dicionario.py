
estado={}

for t in range(0,3):
    est=str(input('Estado: ')).capitalize()
    sig=str(input('Sigla: ')).upper()
    estado[est]=sig



    print()
print()
print(70*'-=')
for s in estado.keys():
    print(s)
print()
for i in range(0,3):
    per=str(input('Quer saber a sigla de qual estado?: '))
    print(estado[per])
    print()

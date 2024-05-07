from time import sleep
l=[]
def cont(a,b,c):
        d=0
        if a>b :

                for f in range(a, c):

                        l.append(f)
                    
                                


        else:
                
                for i in range(a,c):
                        d+=b
                        print(d,end=' ')
                        sleep(0.3)




print('Contagem do 1 ate 10 (de 1 em 1):')
cont(0,1,10)
print()
print('Contagem de 10 ate 0 (de 2 em 2):')
cont(10,2,0)
print(l)
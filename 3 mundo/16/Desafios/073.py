times = ('Atlético-MG', 'Palmeiras', 'Fortaleza', 'Bragantino', 'Flamengo', 'Corinthians', 'Internacional', 'Athletico-PR', 'Ceará SC', 'Santos', 'Atlético-GO', 'Bahia', 'Fluminense', 'Sport Recife', 'Juventude', 'São Paulo', 'América-MG', 'Cuiabá Esporte Clube', 'Grêmio', 'Chapecoense')
print('\033[32m==\033[33m=== \033[1;34mCAMPEONATO BRASILEIRO\033[33m ===\033[32m==\033[m')
for cla in range(1,21):
    print(f'\033[34m{cla}º\033[m',times[cla-1])
print()
print('     \033[1:32mOS 5 PRIMEIROS SAO:\033[m')
for cincop in range(1,6):
    print(f'\033[32m{cincop}º\033[m',times[cincop-1])

print()
print('     \033[1:31mOS 5 ULTIMOS SAO:\033[m')
for cincou in range(15,21):
    print(f'\033[31m{cincou}º\033[m',times[cincou-1])

print()
po=times.index('Chapecoense')
print(f'A \033[32mCHAPECOENSE\033[m esta na \033[31m{po+1}º\033[m posiçao')








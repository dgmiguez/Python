from random import randint, sample
from time import sleep
# com sample
'''mega = list()
mega2 = list()
print('*+'*15)
print(f'{'JOGO DA MEGA SENA':^30}')
print('*+'*15)
choice = int(input('Quantos palpites deseja? '))
for c in range(choice):
    palpite = sample(range(1, 61), 6)
    mega.append(palpite)
    mega2.append(mega[:])
    mega.clear()
print('*+'*3, f'SORTEANDO {choice} JOGOS', '*+'*3)
for v in range(len(mega2)):
    print(f'Jogo {v+1}: {sorted(mega2[v])}')
    sleep(0.5)
print('*+'*3, f'{'  BOA SORTE  '}', '*+'*3)'''

# sem sample
mega = list()
mega2 = list()
print('-'*30)
print('JOGO DA MEGA SENA'.center(30))
print('-'*30)
choice = int(input('Quantos palpites você deseja? '))
print('-'*30)
print('SORTEANDO JOGO(S)'.center(30))
print('-'*30)
for p in range(choice):
    for v in range(6):
        aleatorio = randint(1, 60)
        while aleatorio in mega:
            aleatorio = randint(1, 60)
        mega.append(aleatorio)
    mega2.append(mega[:])
    mega.clear()
for l in range(len(mega2)):
    print(sorted(mega2[l]))
    sleep(0.5)

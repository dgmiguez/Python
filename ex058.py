from random import  randint
from time import sleep
comp = randint(0, 10)
cont = 1
tent = ''
tentcont = ''
print('Olá! vamo jogar?\n'
      'Estou pensando em um número entre 1 e 10...')
sleep(1)
eu = int(input('Qual número eu pensei? '))
while eu != comp:
    if comp > eu:
        tent = 'Mais.'
    else:
        tent = 'Menos.'
    print(f'Você errou, tente {tent}.')
    eu = int(input('Qual foi o número: '))
    cont += 1
if cont == 1:
    tentcont = 'tentativa'
else:
    tentcont = 'tentativas'
print(f'Você acertou! precisou de {cont} {tentcont}.')

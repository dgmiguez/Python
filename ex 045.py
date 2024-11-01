from random import randint
from time import sleep
item = ('Pedra', 'Papel', 'Tesoura')
print('Vamos jogar Jo Ken Po?')
jogador = int(input('[0]Pedra.\n[1]Papel.\n[2]Tesoura.\nEscolha uma das opções acima: '))
#  0 > 2, 1 > 0, 2 > 1 parâmetro de comparação.
comp = randint(0, 2)
print('\033[32mJO\033[m')
sleep(1)
print('\033[033mKEN\033[m')
sleep(1)
print('\033[31mPO\033[m')
sleep(1)
if jogador >= 3:
    print('Opção Inválida. Você foi DESCLASSIFICADO! HA HA HA')
else:
    print('Jogador escolheu {}.\nComputador escolheu {}.'.format(item[jogador], item[comp]))
if jogador == 0 and comp == 2:
     print('Jogador GANHOU!')
elif jogador == 1 and comp == 0:
    print('Jogador GANHOU!')
elif jogador == 2 and comp == 1:
    print('Jogador GANHOU!')
elif comp == 0 and jogador == 2:
    print('Computador GANHOU!')
elif comp == 1 and jogador == 0:
    print('Computador GANHOU!')
elif comp == 2 and jogador == 1:
    print('Computador GANHOU')
elif comp == jogador:
    print('Jogo EMPATADO')

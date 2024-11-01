from random import randint, random
from operator import itemgetter
resultado = {'jogador 1': randint(1, 6),
             'jogador 2': randint(1, 6),
             'jogador 3': randint(1, 6),
             'jogador 4': randint(1, 6)}
print('+-' * 15, end='+''\n')
print('JOGO DE DADOS'.center(30))
print('+-' * 15, end='+''\n')
for k, v in resultado.items():
    print(f'O {k} tirou {v} no dado')
print('+-' * 15,end='+''\n')
print('RESULTADO'.center(30))
print('+-' * 15, end='+''\n')
#ranking = list() - não precisa desta lista
ranking = sorted(resultado.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(ranking):
    print(f'{i+1}° lugar: {v[0]} com {v[1]} pontos.')

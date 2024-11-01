jogador = dict()
gols_temp = 0
gols = list()
cont = 0
print('+-' * 15, end='+''\n')
print('Gerenciamento de Jogador'.center(30))
print('+-' * 15, end='+''\n')
jogador['Nome'] = str(input('Nome: ')).strip()
partidas = int(input('Total de Partidas:  '))
for g in range(partidas):
    gols_temp = int(input(f'Gols da {g + 1}° partida: '))
    cont += gols_temp
    gols.append(gols_temp)
jogador['Gols'] = gols
jogador['Total de Gols'] = cont
print('+-' * 15, end='+' '\n')
print(jogador)
print('+-' * 15, end='+''\n')
for k, v in jogador.items():
    print(f'  - {k}: {v}')
print('+-' * 15, end='+''\n')
print(f'O jogador {jogador['Nome']} jogou {partidas} partidas.')
for i in range(len(gols)):
    print(f' => Na {i + 1}° partida, fez {gols[i]} gol(s).')
print(f'Foi um total de {cont} gols.')


'''jogador = dict()
gols = list()
print('+-' * 15, end='+''\n')
print('Gerenciamento de Jogador'.center(30))
print('+-' * 15, end='+''\n')
jogador['Nome'] = str(input('Nome: ')).strip()
partidas = int(input('Total de Partidas:  '))
for g in range(partidas):
    gols.append(int(input(f'Gols da {g + 1}° partida: ')))
jogador['Gols'] = gols
jogador['Total de Gols'] = sum(gols)
print('+-' * 15, end='+' '\n')
print(jogador)
print('+-' * 15, end='+''\n')
for k, v in jogador.items():
    print(f'  - {k}: {v}')
print('+-' * 15, end='+''\n')
print(f'O jogador {jogador['Nome']} jogou {partidas} partidas.')
for i in range(len(gols)):
    print(f' => Na {i + 1}° partida, fez {gols[i]} gol(s).')
print(f'Foi um total de {jogador['Total de Gols']} gols.')'''

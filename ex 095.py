jogador = dict()
gols = list()
time = list()
while True:
    jogador.clear()
    jogador['Nome'] = str(input('Nome do jogador: '))
    partidas = int(input(f'Quantos partidas {jogador['Nome']} jogou? '))
    for p in range(partidas):
        gols.append(int(input(f'Quantos gols {jogador['Nome']} fez na {p+1}° partida? ')))
    jogador['gols'] = gols[:]
    jogador['Total'] = sum(gols[:])
    time.append(jogador.copy())
    gols.clear()
    while True:
        choice = str(input('Quer continuar? [S/N] '))
        if choice in 'NnSs':
            break
        print('ERRO! Escolha apenas S ou N.')
    if choice in 'Nn':
        break
print(f'{'cod'}', end=' ')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('_'*40)
for k, v in enumerate(time):
    print(f'{k:>3}', end=' ')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
while True:
    dados = int(input('Mostrar os dados de qual jogador? [999 para] '))
    if dados == 999:
        break
    if dados >= len(time):
        print('ERRO! Código de jogador não encontrado')
    else:
        print(f'-- MOSTRANDO DADOS DO JOGADOR {time[dados]['Nome']}')
        for i, c in enumerate(time[dados]['gols']):
            print(f'   No jogo {i+1} fez {c}')

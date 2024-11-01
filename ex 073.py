time = ('Flamengo', 'Bahia', 'Botafogo', 'São Paulo', 'Athletico-PR',
        'Bragantino', 'Palmeiras', 'Internacional', 'Cruzeiro', 'Atlético-MG',
        'Fortalez', 'Grêmio', 'Vasco da Gama', 'Juventude', 'Fluminense',
        'Criciúma', 'Corinthians', 'Atlético-GO', 'EC Vitória', 'Cuiabá')
print('-°' * 135)
print(f'\033[1:34mLista dos times do campeonato brasileiro\033[m:\n {time}')
print('-°' * 135)
print(f'\033[1:32mOs 5 primeiros times são\033[m\n {time[0:5]}')
print('-°' * 135)
print(f'\033[1:31mOs 4 últimos times são\033[m\n {time[-4:]}')
print('-°' * 135)
print(f'\033[1:34mTimes em ordem alfabética\033[m:\n {sorted(time)}')
print('-°' * 135)
print(f'\033[1:33mO internacional está na {time.index("Internacional") + 1}ª posição\033[m')
print('-°' * 135)

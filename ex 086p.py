matriz = [[], [], []]
for l in range(3):
    for c in range(3):
        matriz[l].append(int(input(f'Digite um valor para [{l},{c}]: ')))
print('*+'*15)
print(f'{'MATRIZ':^30}')
print('*+'*15)
for l in range(3):
    for c in range(3):
        print(f'[\033[1:34m{matriz[l][c]:^6}\033[m]', end=' ')
    print()

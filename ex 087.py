matriz = [[], [], []]
soma_pares = soma_terceira = maior = 0
for l in range(3):
    for c in range(3):
        matriz[l].append(int(input(f'Digite um valor para [{l},{c}]: ')))
for l in range(3):
    soma_terceira += matriz[l][2]
    for c in range(3):
        if matriz[l][c] % 2 == 0:
            soma_pares += matriz[l][c]
        if matriz[1][c] > maior:
            maior = matriz[1][c]
print('*+'*15)
for l in range(3):
    for c in range(3):
        print(f'[{matriz[l][c]:^6}]', end=' ')
    print()
print('*+'*15)
print(f'Soma de todos os valores pares da matriz: {soma_pares}')
print(f'Soma dos valores na terceira coluna: {soma_terceira}')
print(f'Maior valor da linha [2]: {maior}')

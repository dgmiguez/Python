valor = list()
for n in list(range(0, 5)):
    valor.append(int(input(f'Digite um valor para a posição {n}: ')))
print(f'Você digitou os valores ', end='')
for v in valor:
    print(end='' f'{v} ')
ma = max(valor)
mi = min(valor)
print(f'\nO maior número foi {ma} nas posições ', end='')
for p, v in enumerate(valor):
    if v == ma:
        print(f'{p}...', end=' ')
print(f'\nO menor número foi {mi} nas posições ', end='')
for p, v in enumerate(valor):
    if v == mi:
        print(f'{p}...', end=' ')

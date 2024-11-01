num = [2, 5, 9, 1]
num[2] = 3
num.append(7)
num.insert(2, 10)
if 2 in num:
    num.remove(2)
    if 5 in num:
        num.remove(1)
else:
    print('Cadê o número 8?')
for n in num:
    print(f'{n}', end=' ')
print('\n', end='')
for i, n in enumerate(num):
    print(f'Na posição {i} eu encontro o número {n}')
print(f'Essa lista tem {len(num)} elementos')
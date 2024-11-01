from random import sample
tup = tuple(sample(range(10), 5))
print(f'Os números sorteados foram ', end='')
for n in tup:
    print(f'{n} ', end='')
print(f'\nO maior número foi {max(tup)}')
print(f'O menor número foi {min(tup)}')

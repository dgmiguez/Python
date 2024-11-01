n = int(input('Digite um número para análise: '))
total = 0
for p in range(1, n+1):
    if n % p == 0:
        total += 1
if total == 2:
    print('primo')
else:
    print('não é primo')

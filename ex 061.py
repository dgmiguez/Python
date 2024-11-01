print('Resolvendo um P.A.')
t = int(input('Digite o primeiro Termo: '))  # termo
r = int(input('Digite a Razão: '))  # razao
t1 = t  # cada termo
cont = 1
print('Os 10 primeiros termos desta P.A. são: ')
while cont <= 10:
    print(f'{t1}', end=' ')
    t1 += r
    cont += 1

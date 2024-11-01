print('\033[1:35m~\033[m' *30)
print('Sequência de Fibonacci')
print('\033[1:35m~\033[m' *30)
n = int(input('Quantos termos deseja mostrar? '))
t1 = 0
t2 = 1
print(f'{t1} - {t2}', end=' - ')
cont = 3
while cont <= n:
    t3 = t1 + t2
    cont += 1
    t1 = t2
    t2 = t3
    print(f'{t3}', end='')
    print(' - ' if cont <= n else '', end='')

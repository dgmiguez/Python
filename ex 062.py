print('Progressão Aritimética')
t1 = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
t = t1
cont = 1
total = 0
dez = 10
while dez != 0:
    total += dez
    while cont <= total:
        print(f'{t}', end=' ')
        print('- ' if cont < total else '', end='')
        t += r
        cont += 1
    print('')
    dez = int(input('Deseja mostrar mais quantos termos? '))

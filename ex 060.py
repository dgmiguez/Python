print('Cálculo de Fatoria!')
n = int(input('Digite um número: '))
cont = n
fat = 1
print(f'{n}! = ', end='')
while cont > 0:
    print(f'{cont} ', end= '')
    print('x ' if cont > 1 else '= ', end='')
    fat *= cont
    cont -= 1
print(fat)

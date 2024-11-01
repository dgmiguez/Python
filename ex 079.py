valor = list()
choice = 's'
while True:
    if choice == 's':
        n = int(input('Digite um valor: '))
        if n not in valor:
            valor.append(n)
        else:
            print('Este número já foi digitado!')
        choice = str(input('Quer continuar? [S/N] '))
        while 'n' != choice != 's':
            print('Entrada inválida')
            choice = str(input('Quer continuar? [S/N] ')).lower()
    else:
        break
print(f'Você digitou os número {sorted(valor)}')

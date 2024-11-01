from time import sleep
option = 0
pv = int(input('Primeiro Valor: '))
sv = int(input('Segudno Valor: '))
while option != 5:
    print('[ 1 ] Soma\n'
          '[ 2 ] Multiplica\n'
          '[ 3 ] Saber o Maior\n'
          '[ 4 ] Novos Números\n'
          '[ 5 ] Encerrar')
    option = int(input('Qual sua opção? '))
    if option == 1:
        print(f'A soma entre {pv} e {sv} é {pv + sv}')
        sleep(1)
    elif option == 2:
        print(f'A multiplicação entre {pv} e {sv} é {pv * sv}')
    elif option == 3:
        if pv > sv:
            maior = pv
        else:
            maior = sv
        print(f'O maior número entre {pv} e {sv} é {maior}')
    elif option == 4:
        pv = int(input('Primeiro Valor: '))
        sv = int(input('Segundo Valor: '))
    elif option == 5:
        print('Programa Encerrado.')
    elif option >= 6:
        print('Opção incorreta!')
    print('-' * 10)
    sleep(1)

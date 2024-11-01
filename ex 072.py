números = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
           'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito',
           'dezenove', 'vinte')

print('~' * 38)
print(f'{'Números por Extenso':^38}')
print('~' * 38)
while True:

    num = int(input('Escolha um número entre 0 e 20: '))
    if 0 > num or num > 20:
        print('Ops! ', end='')

    if 0 <= num <= 20:
        print(f'Você escolheu o número \033[1:31m{números[num]}\033[m')
        print('~' * 38)
        escolha = ' '
        while escolha not in 'SN':
            escolha = str(input('Deseja escolher outro número? [S/N] ')).strip().upper()[0]
        if escolha == 'N':
             break
print('~' * 38)
print('Acabooooooooou!')

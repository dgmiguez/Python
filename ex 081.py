lista = list()
e = 0
while True:
    lista.append(int(input('Digite um valor inteiro: ')))
    e += 1
    choice = str(input('Quer continuar? [S/N] '))
    while choice not in 'NnSs':
        print('Comando INVÁLIDO! tente outra vez.')
        choice = str(input('Quer continuar? [S/N] '))
    if choice in 'n':
        break
print('+*' * 30)
if len(lista) > 1:
    print(f'Você digitou \033[1:33m{e}\033[m elementos')
    print(f'Os valores digitados são', end='')
else:
    print('Você digitou \033[1:33m1\033[m elemento')
    print(f'O valor digitado é', end='')
lista.sort(reverse=True)
for v in lista:
    print(end=' 'f'\033[1:32m{v}\033[m')
if 5 in lista:
    print('\nO número \033[1:31m5\033[m faz parte da lista.')
else:
    print('\nO número \033[1:31m5\033[m não faz parte da lista.')

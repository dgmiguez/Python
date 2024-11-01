lista = list()
lista_par = list()
lista_impar = list()
while True:
    numero = int(input('Digite um número: '))
    if numero % 2 == 0:
        lista_par.append(numero)
        lista.append(numero)
    else:
        lista_impar.append(numero)
        lista.append(numero)
    choice = str(input('Quer continuar? [S/N] ')).lower().strip()
    while choice not in 'sn':
        choice = str(input('Quer continuar? [S/N] ')).lower().strip()
    if choice in 'n':
        break
print(f'A lista completa é {lista}')
print(f'A lista de pares é {lista_par}')
print(f'A lista de ímpares é {lista_impar}')

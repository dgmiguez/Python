from time import sleep
pessoa = list()
totpessoa = list()
peso = list()
mai = men = 0
while True:
    pessoa.append(str(input('Nome: ')))
    pessoa.append(float(input('Peso:')))
    if len(totpessoa) == 0:
        mai = men = pessoa[1]
    else:
        if pessoa[1] > mai:
            mai = pessoa[1]
        if pessoa[1] < men:
            men = pessoa[1]
    totpessoa.append(pessoa[:])
    pessoa.clear()
    choice = str(input('Quer continuar? [S/N] '))
    while choice not in 'SsNn':
        print('É S para SIM e N para Não! Entendeu?')
        sleep(1)
        choice = str(input('Quer continuar? [S/N] '))
    if choice in 'Nn':
        break
print(f'Você Cadastrou um total de {len(totpessoa)} pessoas.')
print(f'O maior peso foi de {mai}Kg. Foram os pesos de ', end='')
for p in totpessoa:
    if p[1] == mai:
        print(f'[{p[0]}]', end='')
print(f'\nO menor peso foi de {men}Kg. Foram os pesos de ', end='')
for p in totpessoa:
    if p[1] == men:
        print(f'[{p[0]}]', end='')
pessoa = dict()
geral = list()
idade = list()
sexo = list()
acima = list()
while True:
    pessoa['Nome'] = str(input('Nome: ')).strip().capitalize()
    while True:
        pessoa['Sexo'] = str(input('Sexo: [M/F]')).strip().upper()
        if pessoa['Sexo'] in 'MmFf':
            break
        else:
            print('ERRO! Digite apenas M ou F.')
    pessoa['Idade'] = int(input('Idade: '))
    geral.append(pessoa.copy())
    idade.append(pessoa['Idade'])
    if pessoa['Sexo'] in 'F':
        sexo.append(pessoa['Nome'])
    choice = str(input('Quer continuar? [S/N] '))
    while choice not in 'SsNn':
        print('ERRO! Digite apenas S ou N.')
        choice = str(input('Quer continuar? [S/N]')).strip()
    if choice in 'Nn':
        break
mi = sum(idade) / len(geral)
print(f'A) Foram cadastradas {len(geral)} pessoas')
print(f'B) A média de idade é de {mi:.2f}')
print(f'C) As mulheres cadastradas foram ',end='')
for p in geral:
    if p['Sexo'] in 'F':
        print(f'{p['Nome']}', end='')
#for i in range(len(sexo)):
    #print(f'{sexo[i]}', end=' ')
print('\n',end='')
print(f'D) Pessoas acima da média: ')
for i in range(len(geral)):
    if geral[i]['Idade'] > mi:
        print(f'    Nome: {geral[i]['Nome']}; Sexo: {geral[i]['Sexo']}; Idade: {geral[i]['Idade']}')

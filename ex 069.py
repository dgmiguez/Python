# ler idade e sexo de várias pessoas
# perguntar se contiua após cada cadastro
# no final, mostrar:
# quantas pessoas tem mais de 18. quantos homens foram cadastrados e quantas mulheres tem menos de 20.
homemtot = mais18 = mulheresmenos20 = 0
print('~'*35)
print(f'{'Cadastro de Pessoas':^35}')
print('~'*35)
while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = input('Sexo: [M/F] ').upper().strip()[0]
    continuar = ' '
    while continuar not in 'SN':
        continuar = input('Deseja Cadastrar Mais? [S/N] ').upper().strip()[0]
    print('~'*35)
    if idade >= 18:
        mais18 += 1
    if sexo == 'M':
        homemtot += 1
    if idade < 20 and sexo == 'F':
        mulheresmenos20 += 1
    if continuar not in 'S':
        break
print(f'Maiores de 18 anos: {mais18}\n'
      f'Total de Homens: {homemtot}\n'
      f'Mulheres com menos de 20 anos: {mulheresmenos20}')

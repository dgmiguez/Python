# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
# No final do programa, mostre: a média de idade do grupo,
# qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.

media = 0
velho = 0
abaixo20 = 0
nome = ''
idade = ''
mulher = ''
ano = ''
for p in range(1, 5):
    print(f'_____ {p}° pessoa _____')
    name = input('Nome: ')
    age = int(input('Idade: '))
    sex = str(input('Sexo F/M: ')).upper()
    media += age / 4
    if sex == 'M':
        velho == age
        if age > velho:
            velho = age
            nome = name
            idade = age
            print(idade)
    else:
        if sex == 'F':
            if age < 20:
                abaixo20 += 1
                if abaixo20 == 1:
                    mulher = 'mulher'
                else:
                    mulher = 'mulheres'
        mulher = 'mulheres'
print(f'A idade média do grupo é de {media} anos.')
if velho:
    if idade == 1:
        ano = 'ano'
    else:
        ano = 'anos'
    print(f'O homem mais velho tem {idade} {ano} de idade e se chama {nome}.')
else:
    print('Não há HOMENS na pesquisa!')
if abaixo20 > 0:
    print(f'Há {abaixo20} {mulher} com menos de 20 anos.')
else:
    print('Não há MULHERES na pesquisa!')

'''idadehomem = 0
nomevelho = ''
media = 0
totmulher = 0
for p in range (1, 5):
    print(f'_____ {p}° pessoa _____')
    nome = input('Nome: ').strip()
    idade = int(input('Idade: '))
    sexo = input('Sexo (F/M): ').strip()
    media += idade / 4
    if p == 1 and sexo in 'Mm':
        idadehomem = idade
        nomevelho = nome
    if idade > idadehomem and sexo in 'mM':
        idadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade <20:
        totmulher += 1
print(f'A média de idade do grupo é de {media} anos.')
print(f'O homem mais velho tem {idadehomem} anos e se chama {nomevelho}.')
print(f'O total de mulheres abaixo de 20 anos é {totmulher}')'''

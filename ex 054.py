from datetime import date
ano = date.today().year
maior = 0
menor = 0
for pessoa in range(1, 8):
    data = ano - int(input(f'Qual o ano a {pessoa}° pessoa nasceu? '))
    if data >= 18:
        maior += 1
    else:
        menor += 1
print(f'Total de pessoas maiores de idade: {maior}\nTotal de pessoas menores de idade: {menor}')

from datetime import date
cadastro = dict()
cadastro['nome'] = str(input('Nome: ')).strip()
nasc = int(input('Ano de Nascimento: '))
cadastro['Idade'] = date.today().year - nasc
cadastro['CTPS'] = int(input('Carteira de Trabalho (0 não tem): '))
if cadastro['CTPS'] != 0:
    cadastro['Ano de Contratação'] = int(input('Ano de Contratação: '))
    cadastro['Salário'] = float(input('Salário: R$'))
    cadastro['Aposentadoria'] = (cadastro['Ano de Contratação'] + 35) - nasc
for k, v in cadastro.items():
    print(f' - {k} tem o valor {v}')

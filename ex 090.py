aluno = dict()
aluno['nome'] = str(input('Nome: ')).strip()
aluno['media'] = float(input(f'Média de {aluno['nome']}: '))
if aluno['media'] < 5:
    aluno['situação'] = f'{'\033[1:31mREPROVADO\033[m'}'
elif 5<= aluno['media'] < 7:
    aluno['situação'] = 'EM RECUPERAÇÃO'
else:
    aluno['situação'] = f'{'\033[1:32mAPROVADO\033[m'}'
print('-_'*17)
print(f'  - Nome do aluno: \033[34m{aluno['nome']}\033[m\n'
      f'  - Média do aluno: \033[33m{aluno['media']}\033[m\n'
      f'  - Situação do aluno: {aluno['situação']}')

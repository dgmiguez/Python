aluno = list()
while True:
     nome = str(input("Nome: "))
     nota1 = float(input('Nota 1: '))
     nota2 = float(input('Nota 2: '))
     media = (nota1 + nota2) / 2
     aluno.append([nome, nota1, nota2, media])
     choice = str(input('Quer continuar? [S/N]: '))[0:1]
     while choice not in 'SsnN':
         print('DIGITE UMA OPÇÃO VÁLIDA')
         choice = str(input('Quer continuar? [S/N]: '))[0:1]
     if choice in 'Nn':
         break
print(f'{'N°':<3} {'NOME':<7} {'MÉDIA':>5}')
print('-'*20)
for v in range(len(aluno)):
    print(F'{v:<3} {aluno[v][0]:<7} {aluno[v][3]:>5}')
print('-'*20)
while True:
    show = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    while 999 != show not in range(len(aluno)):
        print('Não existe essa matrícula!')
        show = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if show == 999:
        print('*----- ATÉ MAIS VER! -----*')
        break
    print(f'Notas de {aluno[show][0]} são [{aluno[show][1]}, {aluno[show][2]}]')

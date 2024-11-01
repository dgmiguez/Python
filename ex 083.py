ex = input('Digite uma expressão matemática: ')
parenteses_abertos = 0
parenteses_fechados = 0
for v in ex:
    if v in '(':
        parenteses_abertos += 1
    if v in ')':
        parenteses_fechados += 1
if parenteses_abertos != parenteses_fechados:
    print('Expressão inválida!')
else:
    print('Expressão válida!')

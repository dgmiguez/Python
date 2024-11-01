lista = list()
ex = str(input('Digite uma expressão matemática: '))
for p in ex:
    if p == '(':
        lista.append('(')
    elif p == ')':
        if len(lista) > 0:
            lista.pop()
        else:
            lista.append(')')
            break
if len(lista) == 0:
    print('Sua expressão está válida')
else:
    print('Sua expressão está inválida')
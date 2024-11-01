palavras = ('Armario', 'Mesa', 'Cadeira', 'Cama', 'Sofa')
for p in palavras:
    print(f'\nVogais da palavra {p.upper()}: ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')

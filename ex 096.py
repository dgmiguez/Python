
def traco():
    print('-' * 20)


def area(n1, n2):
    print(f'A área de um terreno de {n1}x{n2} é {n1 * n2}m²')


traco()
print('Controle de Terrenos')
traco()
larg = float(input('LARGURA: '))
comp = float(input('COMPRIMENTO: '))

area(larg, comp)

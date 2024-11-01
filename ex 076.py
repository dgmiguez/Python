from tabulate import tabulate
produtos = (('Pão', 'R$  5,00'), ('Arroz de 5Kg', 'R$ 23,00'),('Manteiga', 'R$  5,97'))
tab = tabulate(produtos, headers = ['Produto', 'Preço'])
print(tab)

'''produtos = ('Pão', 5,
            'Arroz', 23,
            'Manteiga', 5.97)
print('_+_+'*6)
print(f'{'LISTA DE PREÇOS':^24}')
print('_+_+'*6)
for prod in range(0, len(produtos)):
    if prod % 2 == 0:
        print(f'{produtos[prod]:.<15}', end='')
    else:
        print(f'R${produtos[prod]:>6.2f}')'''
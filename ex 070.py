# ler nome e preço de vários produtos
# vai continuar?
# mostrar total gasto, quantidade de produtos acima de R$ 1000,00, qual o nome do produto mais caro.

totgasto = totacima = prebarato = cont = 0
prodbarato = ''
print('~'*40)
print(f'{'Atacado e Partido':^40}')
print('~'*40)
while True:
    prod = str(input('Produto: ')).strip()
    pre = float(input('Preço: R$'))
    print('~'*40)
    totgasto += pre
    cont += 1
    if pre > 1000:
        totacima += 1
    if cont == 1 or pre < prebarato:
        prebarato = pre
        prodbarato = prod
    conti = ' '
    while conti not in 'SN':
        conti = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
        print('~'*40)
    if conti == 'N':
        break
print(f'Você gastou um total de {totgasto}.')
print(f'Comprou {totacima} produtos acima de R$1000.00.')
print(f'O produto mais barato foi {prodbarato}.')
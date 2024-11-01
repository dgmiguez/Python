preço = float(input('Qual o valor do produto? R$ '))

print('{}\n1 - À vista em dinheiro/Cheque.\n2 - Á vista no cartão.\n'
      '3 - Em até 2x no cartão.\n4 - 3x ou mais no cartão.'.format('FORMAS DE PAGAMENTO'))
opção = int(input('Qual a forma de pagamento? '))
if opção == 1:
    total = preço - (preço * 10/100)  # preço com 10% de desconto
elif opção == 2:
    total = preço - (preço * 5/100)  # preço com 5% de desconto
elif opção == 3:
    total = preço
    print('Sua compra foi parcela em 2x de R${:.2f}'.format(preço/2))
elif opção == 4:
    parcela = int(input('Parcelado em quantas vezes? '))
    total = preço + (preço * 20/100)  # preço com 20% de juros
    print('Sua compra foi parcelada em {}x de R${:.2f}'.format(parcela, total/parcela))
else:
    total = 0  # caso digitem uma opção invalida
    print('Esta opção é inválida. Tente novamente.')
print('O valor total da sua compra é de R${:.2f}'.format(total))
print('OBRIGADO PELA COMPRA')

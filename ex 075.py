cont = 0
cont9 = 0
cont3 = 0
valor = (int(input('Digite um número: ')),
         int(input('Digite outro número: ')),
         int(input('Digite mais um número: ')),
         int(input('Agora um último: ')))
if 9 in valor:
    print(f'O número 9 apareceu {valor.count(9)} vezes.')
else:
    print('Número 9 ausente')
if 3 in valor:
    print(f'O número 3 apareceu na {valor.index(3)+1}° posição.')
else:
    print('Número 3 ausente.')
print(f'Os números pares foram:', end=' ')
for n in valor:
    if n % 2 == 0:
        print(n, end=' ')



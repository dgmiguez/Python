# ler números inteiros pelo teclado
# parar quando 999 for digitado (flag)
# mostrar quantos números foram digitados
# mostrar soma entre eles (desconsiderando a flag)
cont = soma = 0
print('Para terminar o programa, digite 999.')
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    cont += 1
    soma += n
if cont == 1:
    print(f'Você digitou {cont} número.\n'
      f'A soma entre eles foi {soma},')
else:
    print(f'Você digitou {cont} números,\n'
          f'A soma entre eles foi {soma}')

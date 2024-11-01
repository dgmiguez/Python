media = maior = menor = soma = cont = 0
continuar = ''
while continuar != 'N':
    n = int(input('Digite um núrero inteiro: '))
    cont += 1
    soma += n
    if cont == 1:
        maior = n
        menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    continuar = str(input('Deseja continuar? ')).upper()
    while continuar != 'S' and continuar != 'N':
        continuar = str(input('Entrada invalida.\nDigite S ou N.\nDeseja continuar? ')).upper()
media = soma / cont
print(f'Você digitou {cont} números.\nA soma entre eles foi {soma}. Sua média foi {media}.\n'
      f'O maior número foi {maior} e o menor número foi {menor}')

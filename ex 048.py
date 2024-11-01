soma = 0  # acumulador
cont = 0  # contador
for mult in range(1, 501, 2):  # 2 no final pra pegar somente os números ímpares
    if mult % 3 == 0:  # múltiplo de 3
        soma = soma + mult
        cont = cont + 1
print(f'A soma dos {cont} números impares múltipols de 3 entre 1 e 500 é {soma}')

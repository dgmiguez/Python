pesado = 0
leve = 0
for pessoa in range(1, 6):
    peso = float(input(f'Peso da {pessoa}° pessoa: '))
    if pessoa == 1:
        pesado = peso
        leve = peso
    else:
        if peso > pesado:
            pesado = peso
        if peso < leve:
            leve = peso
print(f'O maior peso lido foi {pesado}Kg.\nO menor peso lido foi {leve}Kg.')

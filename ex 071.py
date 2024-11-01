# simular funcionamento de caixa eletrônico.
# perguntar valor sacado (int).
# Program vai informar quantas cédulas de cada valor serão entregues.
# cédulas de R$50, R$20, R$10 e R$1.

valor = int(input('Quanto deseja sacar? R$'))
total = valor
ced = 200
totced = 0
while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced > 0:
            print(f'Total de {totced} cédulas de R${ced}.')
        if ced == 200:
            ced = 100
        elif ced == 100:
            ced = 50
        elif ced == 50:
            ced = 10
        elif ced == 10:
            ced = 5
        elif ced == 5:
            ced = 2
        elif ced == 2:
            ced = 1
        totced = 0
        if total == 0:
            break

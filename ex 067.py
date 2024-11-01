# mostrar tabuada solicitada pelo usuário
# interromper caso seja solicitado valor negativo
print('~'*20)
print(f'{'Tabuada':^20}')
print('~'*20)
cont = 0
print('Para encerrar, digite um número negativo.')
while True:
    n = int(input('Qual tabuada deseja visualizar? '))
    if n < 0:
        break
    while cont < 10:
        cont += 1
        mult = cont * n
        print(f'{n} x {cont:>2} = {mult:>2}')
        if cont == 10:
            cont = 0
            break
print('Tabuada encerrada.')
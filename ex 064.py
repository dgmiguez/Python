cont = -1
soma = -999
n = 0
print('\033[1:36m~\033[m'*50)
print('Vamos fazer a soma de alguns números!')
print('\033[1:36m~\033[m'*50)
print('Para encerrar, digite \033[1:33m999\033[m.')
while n != 999:
    n = int(input('Digite um número inteiro: '))
    cont += 1
    soma += n
print(f'Você digitou \033[1:31m{cont}\033[m números e sua soma foi \033[1:31m{soma}\033[m.')

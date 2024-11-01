matriz = [[], [], [],
          [], [], [],
          [], [], []]
n = 6
'''matriz[0].append(int(input('Digite um valor para [0,0]: ')))'''
for i in range(3):
    matriz[i].append(int(input(f'Digite um valor para [0,{i}]: ')))
for i in range(3, 6):
    matriz[i].append(int(input(f'Digite um valor para [1,{i-3}]: ')))
for i in range(3):
    matriz[n].append(int(input(f'Digite um valor para [2,{i}]: ')))
    n += 1
print(f'{matriz[0]}{matriz[1]}{matriz[2]}')
print(f'{matriz[3]}{matriz[4]}{matriz[5]}')
print(f'{matriz[6]}{matriz[7]}{matriz[8]}')

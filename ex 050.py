acum = 0
for n in range(1, 7):
    num = int(input('Digite um número inteiro: '))
    if num % 2 == 0:
        acum += num
print(f'A soma dos números pares é {acum}')

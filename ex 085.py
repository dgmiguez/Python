valores = list()
par = list()
impar = list()
for v in range(7):
    num = int(input(f'Digite o {v+1}° valor: '))
    if num % 2 == 0:
        par.append(num)
    else:
        impar.append(num)
valores.append(sorted(par[:]))
valores.append(sorted(impar[:]))
par.clear()
impar.clear()
print(f'Foram digitados {len(valores[0])} valores pares: {valores[0]}')
print(f'Foram digitados {len(valores[1])} Valores ímpares: {valores[1]}.')

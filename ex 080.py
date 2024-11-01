valor = list()
for n in range(0, 5):
    num = (int(input('Digite um valor: ')))
    if n == 0 or num > valor[-1]:
        valor.append(num)
        print(f'Adicionado no final da lista.')
    else:
        pos = 0
        while pos < len(valor):
            if num <= valor[pos]:
                valor.insert(pos, num)
                print(f'Adicionado na posição {pos} da lista.')
                break
            pos += 1
print(valor)
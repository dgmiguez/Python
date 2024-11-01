def soma(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma de {a} + {b} = {s} ')


soma(2, 5)
soma(7, 3)
soma(15, 9)
soma(a=3, b=4)
print()

def cont(*num):
    tam = len(num)
    print(f'Recebi os valores {num} e ao todo são {tam} números.')


cont(1,2,3,4,5,6)
cont(6,3,4)
print()

def dobraValores(lista):
    pos = 0
    while pos < len(valores):
        lista[pos] *= 2
        pos += 1
    print(f'A valores dobrados são {valores}.')


valores = [4, 6, 7, 8]
#valores.append(int(input('Digite um valor: ')))
dobraValores(valores)


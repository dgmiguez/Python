from time import sleep
def cont(a, b, c):
    if c == 0:
        c = 1
    if c < 0:
        c *= -1
    print(f'Contagem de {a} até {b} de {c} em {c}')
    sleep(2)
    n = a
    if a < b:
        while n <= b:
            print(n,end=' ', flush=True)
            n += c
            sleep(.5)

    else:
        n = a
        while n >= b:
            print(n, end=' ', flush=True)
            n += -c
            sleep(.5)

    print('')

def linha():
    print('-'*30)


linha()
cont(1, 10, 1)
linha()
cont(10, 0, 2)
linha()
print('Escolha a contagem personalizada')
n1 = int(input('Início: '))
n2 = int(input('Fim:> '))
n3 = int(input('Passo: '))
linha()
cont(n1, n2, n3)
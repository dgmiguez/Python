from random import randint
print('~'*20)
print(f'{'Par ou Ímpar':^20}')
cont = 0
while True:
    print('~'*20)
    jog = int(input('Digite um número: '))
    print('~'*20)
    comp = randint(1, 10)
    escolha = str(input('Par ou Ímpar? [P/I]: ')).upper()
    if escolha == 'P':
        if (jog + comp) % 2 == 0:
            cont += 1
            print(f'Você escolheu {jog} e o computador escolheu {comp},totalizando {jog + comp}!\n'
                  f'Você ganhou!\n'
                  f'Vamos mais uma vez!')
        else:
            print(f'Você escolheu {jog} e o computador escolheu {comp}, totalizando {jog + comp}!\n'
                  f'Você Perdeu!')
            escolha = 'p'
    if escolha == 'p':
        break
    if escolha == 'I':
        if (jog + comp) % 2 == 1:
            cont += 1
            print(f'Você escolheu {jog} e o computador escolheu {comp}, totalizando {jog + comp}!\n'
                  f'Você Ganhou!\n'
                  f'Vamos mais uma vez!')
        else:
            print(f'Você escolheu {jog} e o computador escolheu {comp}, totalizando {jog + comp}!\n'
                  f'Você Perdeu!')
            escolha = 'p'
        if escolha == 'p':
            break
print(f'Fim de Jogo! Você ganhou {cont}')

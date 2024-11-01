print('Vamos encontar os \033[1:31m10\033[m primeiros termos de uma P.A!')
t1 = int(input('Digite o primeiro Termo: '))
r  = int(input('Digite a razão: '))
for t1 in range(t1, 10 * r, r):
    print(t1, end='-')
print('Done')

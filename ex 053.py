p = str(input('Digite uma frase: ')).upper().strip()
separado = p.split()
junto = ''.join(separado)
inverso = ''
for f in range(len(junto) - 1, -1, -1):
    inverso += junto[f]
print(f'O inverso de {junto} é {inverso}')
if inverso == junto:
    print('É palíndromo')
else:
    print('Não é palíndromo')

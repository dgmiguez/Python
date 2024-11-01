teste = list()
teste.append('Dg')
teste.append(40)
irma = list()
irma.append(teste[:])
teste[0] = 'Larissa'
teste[1] = 42
irma.append(teste[:])
print(irma)

galera = [['Dg', 40], ['Fernando', 41], ['Joilson', 46], ['Jamal', 30]]
print(galera)
print(galera[2][1])
print(galera[3][0])
print(galera[0][1])
print(galera[1][0])
for p in galera:
    print((p[1]), (p[0]))

grupo = list()
dado = list()
for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    grupo.append(dado[:])
    dado.clear()
totmai = totmen = 0
for p in grupo:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade.')
        totmai += 1
    else:
        print(f'{p[0]} é menor de idade.')
        totmen += 1
print(f'Temos um total de {totmai} maiores de idade e {totmen} menores de idade.')
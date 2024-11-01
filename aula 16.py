lanche = ('hamburguer', 'suco', 'pizza', 'pudim')
#for comida in lanche:
#    print(f'Eu vou comer {comida}.')

#for comida in range(0, len(lanche)):
#    print(f'Eu vou comer {lanche[comida]}')

for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')

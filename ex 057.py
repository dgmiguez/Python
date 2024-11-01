sexo = input('Digite seu sexo: ').upper().strip()  #coloca [0] para ler somente a primeira letra
while sexo != 'F' and sexo != 'M':  # while sexo not in 'MmFf':
    sexo = input('Sexo incorreto. Por favor, digite seu sexo: ').upper().strip()
print(f'Sexo \033[1:33m{sexo}\033[m válido')
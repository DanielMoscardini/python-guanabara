# Receba o sexo da pessoa e caso digite errado, peca novamente.
sexo = input('Informe seu sexo: [M/F] ').strip().upper()
while sexo not in 'MF':
    sexo = input('Dados Invalidos. Informe seu sexo: [M/F] ').strip().upper()

print(f'Sexo {sexo} cadastrado com sucesso!')

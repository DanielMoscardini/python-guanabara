# Receba um nome e mostre em maiusculo, minusculo, qtde letras total e do primeiro nome.
nome = input('Digite seu nome completo: ').strip()
primeiro_nome = nome.split()
tamanho_nome_completo = len(nome) - nome.count(' ')
print(f'Seu nome em maiúsculo é {nome.upper()}')
print(f'Seu nome em minúsculo é: {nome.lower()}')
print(f'Seu nome tem {tamanho_nome_completo} letras')
print(f'Seu nome é {primeiro_nome[0]} e tem {len(primeiro_nome[0])} letras')

# Receva um nome e verifique a existencia de 'Silva' no nome.
nome = input('Digite seu nome: ').strip()
nome_list = nome.upper().split()
silva = nome_list.count('SILVA')
print('Seu nome tem silva: True') if silva >= 1 else print('Seu nome tem silva: False')

# print(f'Seu nome tem silva {'silva' in nome}')
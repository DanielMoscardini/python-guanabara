# Acha as ocorrências da letra 'A' em um nome:
nome = input('Digite seu nome: ').upper().strip()
print(f'A letra A aparece {nome.upper().count('A')}')
print(f'A primeira letra A apareceu na posição {nome.find('A') + 1}')
print(f'A ultima letra A aparece na posição {nome.rfind('A') + 1}')
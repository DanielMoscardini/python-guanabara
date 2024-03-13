# Verifique se a primeira parte do nome da cidade, começa com santo e retorne true.
cidade = input('Qual cidade voce nasceu? ').strip()
primeiro_nome = cidade.split()[0].upper() # Recebe primeira frase da string cidade.
print('True') if primeiro_nome == 'SANTO' else print('False') # Operador Ternário

# if primeiro_nome == 'SANTO':
#     print('true')
# else:
#     print('false')
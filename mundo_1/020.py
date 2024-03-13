# Receba um número do usuário e verifique se é igual a um número aleatório do sistema.
from random import randint


num_usuario = int(input('Digite um número entre 0 e 5: '))
numero = randint(0, 5)
print(f'ERROU, escolhi o número {numero}') if num_usuario != numero else print('Acertou!')
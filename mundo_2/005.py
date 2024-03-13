# faca um jogo de pedra papel e tesouro
from random import randint


computador = randint(0, 2)
print('[ 0 ] PEDRA')
print('[ 1 ] PAPEL')
print('[ 2 ] TESOURA')
jogador = int(input('Digite sua jogada: '))

if computador == 0 and jogador == 0:
    print(f'EMPATE!')
elif computador == 0 and jogador == 1:
    print(f'Computador: PEDRA - Jogador: PAPEL - Jogador VENCEU')
elif computador == 0 and jogador == 2:
    print(f'Computador: PEDRA - Jogador: TESOURA - Jogador PERDEU')

elif computador == 1 and jogador == 0:
    print(f'Computador: PAPEL - Jogador: PEDRA - Jogador PERDEU')
elif computador == 1 and jogador == 1:
    print(f'EMPATE!')
elif computador == 1 and jogador == 2:
    print(f'Computador: PAPEL - Jogador: TESOURA - Jogador VENCEU')

elif computador == 2 and jogador == 0:
    print(f'Computador: TESOURA - Jogador: PEDRA - Jogador VENCEU')
elif computador == 2 and jogador == 1:
    print(f'Computador: TESOURA - Jogador: PAPEL - Jogador PERDEU')
elif computador == 2 and jogador == 2:
    print(f'EMPATE!')

# Jogue par ou impar com o computador, e continue jogando até perder
from random import randint


ganhou = True
while True:
    if not ganhou:
        break

    computador = randint(0, 10)
    numero_jogador = int(input('Digite um numero: '))
    escolha_jogador = input('Par ou Impar: [P/I] ').upper().strip()
    soma = computador + numero_jogador
    if escolha_jogador == 'P' and soma % 2 == 0:
        print(f'Voce jogou {numero_jogador} e o computador jogou {computador}. Total é {soma} e você ganhou!')
    elif escolha_jogador == 'I' and soma % 2 != 0:
        print(f'Voce jogou {numero_jogador} e o computador jogou {computador}. Total é {soma} e você ganhou!')
    else:
        print(f'Voce jogou {numero_jogador} e o computador jogou {computador}. Total é {soma} e você perdeu!')
        ganhou = False

print('Obrigado por jogar!')

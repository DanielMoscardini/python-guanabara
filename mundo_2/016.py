from random import randint


computador = randint(0, 4)
jogador = int(input('Digite um numero entre 0 e 10: '))
contador = 1

while computador != jogador:
    print('Errou! Tente Novamente!')
    jogador = int(input('Digite um numero entre 0 e 10: '))
    contador += 1

print('Voce acertou!')
print(f'Total de palpites: {contador}')

"""
Receba numeros até a condição de parada, e diga se:
A) Quantos numeros foram digitados.
B) A lista de valores ordenados de forma decrescente.
C) Se o valor 5 está ou não está na lista.
"""
continua = ''
numeros = []
while True:
    numeros.append(int(input('Digite um valor: ')))
    continua = input('Deseja continuar: [S/N] ').upper().strip()

    if continua == 'N':
        break

decrescente = sorted(numeros, reverse=True)
print(f'Você digitou {len(numeros)} elementos')
print(f'Os valores em ordem decrescente: {decrescente}')
if 5 not in numeros:
    print('O valor 5 não foi encontrado na lista')
else:
    print('O valor 5 foi encontrado na lista')


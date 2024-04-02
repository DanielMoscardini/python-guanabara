# Receba numeros, porém caso digitado um numero repetido, não permita e peça outro.
numeros = []
continua = ''
while True:
    n = int(input('Digite um valor: '))
    if n not in numeros:
        numeros.append(n)
        print('Valor adicionado com sucesso!')
    else:
        print('Valor duplicado! Não vou adicionar!')

    continua = input('Deseja continuar? [S/N] ').upper().strip()

    if continua == 'N':
        break

print(numeros)
print('Obrigado por utilizar!')

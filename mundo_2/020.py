# Melhore a tabuada, pedindo outro numero até digitar 0 ou negativo!
while True:
    n = int(input('Quer ver a tabuada de qual valor: '))
    if n <= 0:
        break
    for i in range(1, 11):
        print(f'{n} * {i} = {n * i}')
    print('\n')

print('Obrigado por utilizar!')

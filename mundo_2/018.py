# soma numeros, porem desconsiderar a condicao de parada [999]
cont = soma = 0
num = int(input('Digite um numero: [999 para parar] '))

while num != 999:
    soma += num
    cont += 1
    num = int(input('Digite um numero: [999 para parar] '))

print(f'Voce digitou {cont} numeros e soma deles foi {soma}')

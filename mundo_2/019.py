# Receba numeros até o usuário digitar 999, forneça a qtde de numeros e a soma.
cont = soma = 0

while True:
    numero = int(input('Digite um número: [999 para parar] '))
    if numero == 999:
        break
    cont += 1
    soma += numero

print(f'A soma dos {cont} numeros foi de: {soma}')
print('Obrigado por participar')

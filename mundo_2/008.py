# some os numeros impares e multiplos de tres entre 1 e 500
cont = 0
soma = 0
for i in range(1, 501, 2):
    if i % 3 == 0:
        soma += i
        cont += 1

print(f'A soma dos {cont} valores solicitados eh de: {soma}')

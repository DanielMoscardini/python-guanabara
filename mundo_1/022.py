# leia 3 numeros e mostre qual o maior e qual o menor.
numeros = []
for i in range(0, 3):
    numeros.append(int(input(f'Digite o {i+1}º número: ')))

print(max(numeros))
print(min(numeros))
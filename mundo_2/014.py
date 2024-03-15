# receba 5 pesos e retorne o mais leve e o mais pesado.
pesos = []

for i in range(0, 5):
    pesos.append(float(input(f'Digite o peso da {i} pessoa: ')))

maior_peso = max(pesos)
menor_peso = min(pesos)

print(f'Maior peso: {maior_peso}')
print(f'Menor peso: {menor_peso}')

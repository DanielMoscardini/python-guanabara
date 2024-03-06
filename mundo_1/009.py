# Receba o valor do produto e o desconto aplicado, mostre o valor final.
preco = float(input('Digite o valor do produto: '))
desconto = int(input('Digite o valor do desconto do produto em porcentagem: '))
valor_total = preco - (preco * desconto / 100)
print(f'Valor original: {preco}, desconto: {desconto}%, valor final: {valor_total}')

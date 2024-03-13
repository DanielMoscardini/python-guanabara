# calcule o valor de cada prestacao, nao podendo exceder 30% do salario.
valor_casa = int(input('Digite o valor da casa: '))
salario = int(input('Digite o valor do salario: '))
parcelas = int(input('Digite o em quantos anos quer parelar: '))

mensal = round(valor_casa / (parcelas * 12))
valor_minimo = salario * 30 / 100

if mensal > valor_minimo:
    print(f'O valor da prestacao sera de: {mensal}')
    print(f'NEGADO, o valor da parcela mensal eh maior que 30% do salario')
else:
    print(f'O valor da prestacao sera de: {mensal}')
    print(f'PERMITIDO, o valor da parcela mensal eh menor que 30% do salario')

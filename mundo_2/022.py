total_mais_18 = qtde_homens = mulher_menos_20 = 0

while True:
    idade = int(input('Digite uma idade: '))
    sexo = input('Digite o sexo: [M/F] ').upper().strip()
    continua = input('Quer continuar? [S/N] ')

    if idade > 18:
        total_mais_18 += 1

    if sexo == 'M':
        qtde_homens += 1

    if sexo == 'F' and idade < 20:
        mulher_menos_20 += 1

    if continua == 'N':
        break

print(f'Quantidade de pessoas acima de 18 anos: {total_mais_18}')
print(f'Quantidade de homens: {qtde_homens}')
print(f'Quantidade de mulheres com menos de 20 anos: {mulher_menos_20}')

# calcule o IMC e retorne o status do usuario.
peso = float(input('Digite seu peso (Kg): '))
altura = float(input('Digite sua altura (m): '))
imc = round(peso / (altura * altura), 1)

if imc < 18.5:
    print(f'IMC: {imc} - Abaixo do peso')
elif 18.5 <= imc < 25:
    print(f'IMC: {imc} - Peso ideal')
elif 25 <= imc < 30:
    print(f'IMC: {imc} - Sobrepeso')
elif 30 <= imc < 40:
    print(f'IMC: {imc} - Obesidade')
else:
    print(f'IMC: {imc} - Obesidade Morbida')

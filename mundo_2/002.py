# diga qual numero eh maior ou se ambos sao iguas.
num1 = int(input('Digite o primeiro numero: '))
num2 = int(input('Digite o segundo numero: '))
if num1 > num2:
    print('Primeiro numero eh maior')
elif num1 < num2:
    print('Segundo numero eh maior')
else:
    print('Ambos numeros sao iguais')

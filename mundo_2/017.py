"""
Receba dois numeros e exiba um layout:
1 - somar
2 - multiplicar
3 - maior
4 - novos numeros
5 - sair do programa
"""
num1 = int(input('Digite o primeiro numero: '))
num2 = int(input('Digite o segundo numero: '))

opcao = int(input("""
    [ 1 ] Somar numeros.
    [ 2 ] Multiplicar numeros.
    [ 3 ] Maior numero.
    [ 4 ] Novos numeros.
    [ 5 ] Finalizar programa.
>>>> Qual sua opcao: 
"""))

while opcao != 5:

    if opcao == 1:
        print(f'Soma dos valores: {num1 + num2}')

    elif opcao == 2:
        print(f'Multiplicacao dos valores: {num1 * num2}')

    elif opcao == 3:
        if num1 > num2:
            print(f'Maior dos valores: {num1}')
        elif num2 > num1:
            print(f'Maior dos valores: {num2}')
        else:
            print(f'Valores sao iguais')

    elif opcao == 4:
        num1 = int(input('Digite o primeiro numero: '))
        num2 = int(input('Digite o segundo numero: '))
    else:
        print(f'Opcao invalida! Tente novamente')

    opcao = int(input("""
        [ 1 ] Somar numeros.
        [ 2 ] Multiplicar numeros.
        [ 3 ] Maior numero.
        [ 4 ] Novos numeros.
        [ 5 ] Finalizar programa.
    >>>> Qual sua opcao: 
    """))

print('Obrigado por participar!')

pessoas_temp = []
pessoas = []
maior_peso = menor_peso = 0

while True:
    pessoas_temp.append(input('Nome: ').strip())
    pessoas_temp.append(int(input('Peso: ').strip()))

    if len(pessoas) == 0:
        maior_peso = menor_peso = pessoas_temp[1]
    else:
        if pessoas_temp[1] > maior_peso:
            maior_peso = pessoas_temp[1]
        if pessoas_temp[1] < menor_peso:
            menor_peso = pessoas_temp[1]

    pessoas.append(pessoas_temp[:])
    pessoas_temp.clear()
    resp = input('Deseja continuar? [S/N] ').upper().strip()

    if resp == 'N':
        break

print(f'O maior peso foi de {maior_peso} Kgs, peso de ', end='')
for pessoa in pessoas:
    if pessoa[1] == maior_peso:
        print(f'{pessoa[0]} ', end='')
print('\n')

print(f'O menor peso foi de {menor_peso} Kgs, peso de ', end='')
for pessoa in pessoas:
    if pessoa[1] == menor_peso:
        print(f'{pessoa[0]} ', end='')
print('\n')

print(f'Ao todo, foram cadastradas {len(pessoas)} pessoas')

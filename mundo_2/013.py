# receba diversas datas de nascimento e retorne a qtde de maiores e menores de idade.
from datetime import date


ano = date.today().year
anos = []
maiores = []
menores = []

for i in range(0, 7):
    anos.append(int(input(f'Ano da {i + 1}ª pessoa: ')))
    if ano - anos[i] > 18:
        maiores.append(anos[i])
    else:
        menores.append(anos[i])

print(f'Ao todos tivemos {len(maiores)} pessoas maiores de idade')
print(f'Ao todos tivemos {len(menores)} pessoas menores de idade')

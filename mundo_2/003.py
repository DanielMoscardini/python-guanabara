# calcule a media de duas notas e retorne se o aluno foi aprovado ou reprovado.
n1 = float(input('Digite a primeira nota do aluno? '))
n2 = float(input('Digite a segunda nota do aluno: '))
media = (n1 + n2) / 2

if media < 5.0:
    print(f'Nota {media:.2f} - REPROVADO')
elif 5.0 >= media < 6.9:
    print(f'Nota {media:.2f} - RECUPERACAO')
else:
    print(f'Nota {media:.2f} - APROVADO')

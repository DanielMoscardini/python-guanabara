# Receba um lista de alunos e sorteie o nome de um deles.
from random import choice


alunos = []
for i in range(0, 5):
    alunos.append(input('Qual o nome do aluno? '))

print(choice(alunos))

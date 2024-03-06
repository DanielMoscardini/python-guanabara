# Receba um lista de alunos e sorteie a ordem da lista de forma aleatória
from random import shuffle


alunos = []
for i in range(0, 5):
    alunos.append(input(f'Qual o nome do {i + 1}º aluno? '))

shuffle(alunos)
print(alunos)

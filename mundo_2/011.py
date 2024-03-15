# Receba um numero e diga se ele eh primo ou nao.
num = int(input('Digite um numero: '))
count_primo = 0
count_n_primo = 0
for i in range(1, num + 1):
    if num % i == 0:
        count_primo += 1
    else:
        count_n_primo += 1

if count_primo == 2:
    print(f'O numero {num} eh um numero primo')
else:
    print(f'O numero {num} pode ser dividido {count_n_primo} vezes e nao eh primo')

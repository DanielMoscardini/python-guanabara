# Receba um número inteiro e separe por digítos:
num = int(input('Digite um número: '))
num_len = len(str(num))
num_list = [num]
print(num_len)
print(num_list)
for i in num_list:
    if i == num_list[0]:
        print(f'{i} = Unidade')
    elif i == num_list[1]:
        print(f'{i} = Dezena')
    elif i == num_list[2]:
        print(f'{i} = Centena')
    elif i == num_list[3]:
        print(f'{i} = Milhar')
    else:
        break

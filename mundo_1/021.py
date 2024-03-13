# Se a velocidade for acima de 80, multe por 7 reais a cada km/h excedente.
vel_permitida = 80
vel_usuario = int(input('Digite sua velocidade atual: '))
multa = (vel_usuario - vel_permitida) * 7
if vel_usuario <= vel_permitida:
    print('Pode ir e dirija com segurança!')
else:
    print(f'Multado no valor de: {multa}')
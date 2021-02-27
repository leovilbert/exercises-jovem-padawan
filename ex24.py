semana = ['domingo', 'segunda', 'terça', 'quarta', 'quinta', 'sexta', 'sábado']

dia = int(input('Digite um número de 1 a 7: '))

if 0 < dia < 8:
    print(f'Número {dia} é {semana[dia-1]}!')
else:
    print('Valor inválido')
peso = int(input('Qual o peso de peixes, em kg? '))

print(f'O peso de peixes é de {peso}kg!')

if peso > 50:
    excesso = peso - 50
    multa = excesso * 4
    print(f'O peso excedeu em {excesso}kg e o valor a ser pago pela multa é de R${multa}!')
else:
    print('Não excedeu o peso, então não pagará nenhuma multa!')
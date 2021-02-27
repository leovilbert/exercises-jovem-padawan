anos = int(input('Qual a sua idade em anos? '))
meses = int(input('Meses? '))
dias = int(input('Dias? '))

idade_dias = anos * 365 + meses * 30 + dias

print(f'Sua idade em apenas dias é de {idade_dias} dias.')
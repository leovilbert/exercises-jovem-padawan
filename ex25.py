nota = int(input('Digite uma nota de zero a dez: '))

while nota < 0 or nota > 11:
    nota = int(input('Valor inválido! Digite uma nota de zero a dez: '))

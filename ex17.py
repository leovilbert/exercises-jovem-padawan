area = float(input('Qual o tamanho em metros quadrados da área a ser pintada? '))

lata = round((area / (18 * 3))+ 0.5)

if lata > 1:
    preço = lata * 80
    print(f'Será necessário {int(lata)} latas de tinta', end='')
else:
    preço = 80 
    print(f'Será necessário uma lata de tinta', end='')
print(f' e custará R${preço:.2f} reais.')

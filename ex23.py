turno = str(input('Em que turno você estuda? ')).lower()

if turno == 'matutino':
    print('Bom dia!')
elif turno == 'vespertino':
    print('Boa tarde!')
elif turno == 'noturno':
    print('Boa noite!')
else:
    print('Valor inválido!')
eleitores = int(input('Qual o número total de eleitores do município? '))
votos_brancos = int(input('Qual o número de votos brancos do município? '))
votos_nulos = int(input('Qual o número de votos nulos do município? '))
votos_validos = int(input('Qual o número de votos validos do município? '))

percentual_brancos = round(votos_brancos / eleitores * 100)
percentual_nulos = round(votos_nulos / eleitores * 100)
percentual_validos = round(votos_validos / eleitores * 100)

print(f'''\nBrancos: {percentual_brancos}%
\nNulos: {percentual_nulos}%
\nVálidos: {percentual_validos}%''')
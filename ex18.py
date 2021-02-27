arquivo = float(input('Qual o tamanho do arquivo para download (em MB)? '))

velocidade = float(input('Qual a velocidade da Internet (em Mbps)? '))

tempo_download = (arquivo / velocidade) * 8 / 60

print(f'O tempo estimado é de {tempo_download:.1f} minutos.')
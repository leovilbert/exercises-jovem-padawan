custo_fabrica = int(input('Digite o custo de fábrica de um carro: '))
distribuidor = custo_fabrica * 0.28
impostos = custo_fabrica * 0.45
preço_final = custo_fabrica + distribuidor + impostos

print(f'''O preço de fábrica é de R${custo_fabrica}
Com os custos do distribuidor e os impostos,
O preço final do carro para o consumidor é de R${preço_final:.2f}.''')
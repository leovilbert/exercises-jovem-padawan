salario = int(input('Digite o valor do salário fixo: ')) 
comissao = int(input('Digite o valor da comissão por carro vendido: '))
carros_vendidos = int(input('Digite a quantidade de carros vendidos: '))
total_vendas = int(input('Digite o valor total das vendas: ')) 

salario_final = salario + comissao * carros_vendidos + total_vendas * 5/100

print(f'\nO valor final do salário do funcionário é de R${salario_final:.2f}!')
 
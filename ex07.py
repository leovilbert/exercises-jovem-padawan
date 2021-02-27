salario = int(input('Digite o salário mensal de um funcionário, em reais: '))
reajuste = float(input('Digite o percentual de reajuste: '))
novo_salario = salario + (salario * reajuste / 100) 

print(f'O novo salários será de R${novo_salario:.2f}.')
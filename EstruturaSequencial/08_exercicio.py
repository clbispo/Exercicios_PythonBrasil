#8 - Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.
valor_hora = float(input("Quanto você ganha por hora? "))
n_horas = float(input("Quantas horas trabalha no mês? "))

salario = valor_hora * n_horas
print(f"Total do salário no mês: R$ {salario:.2f}")
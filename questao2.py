# Entrada de dados
salario = float(input("Digite o salário: R$ "))

# Cálculo da bonificação
if salario <= 500:
    bonus = salario * 0.05
elif salario <= 1200:
    bonus = salario * 0.12
else:
    bonus = 0

# Novo salário
novo_salario = salario + bonus

# Saída
print(f"Salário original: R$ {salario:.2f}")
print(f"Bonificação: R$ {bonus:.2f}")
print(f"Novo salário: R$ {novo_salario:.2f}")

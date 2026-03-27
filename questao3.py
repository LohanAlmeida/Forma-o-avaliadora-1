# Entrada de dados
salario = float(input("Digite o salário: R$ "))
idade = int(input("Digite a idade: "))

# Verificação das condições
if salario >= 1600 and idade >= 18:
    bonus = 1000
    novo_salario = salario + bonus
    
    print(f"Novo salário com bonificação: R$ {novo_salario:.2f}")
else:
    print("Não há bonificação.")

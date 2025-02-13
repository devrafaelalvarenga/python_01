#Cálculo de KPI

nome_usuario = str(input('Digite seu nome: ')).title()  # .title() deixa a primeira letra de cada palavra em maiúsculo
valor_salario = float(input('Digite o valor do seu salário: '))
valor_bonus = float(input('Digite o valor do seu bônus: '))
valor_variavel = 1000

valor_kpi = valor_variavel + (valor_salario * valor_bonus)
print(f'{nome_usuario}, o valor do seu bonus é: {valor_kpi:.2f}') # :.2f para mostrar apenas 2 casas decimais
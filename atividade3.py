def calcular_reajuste(salario_atual):
   
    if salario_atual <= 250:
        percentual_aumento = 15
    elif salario_atual <= 900:
        percentual_aumento = 25
    elif salario_atual <= 1800:
        percentual_aumento = 20
    else:
        percentual_aumento = 10

    
    valor_aumento = salario_atual * (percentual_aumento / 100)
    
   
    novo_salario = salario_atual + valor_aumento
    
    
    inflacao = 3.8
    valor_aumento_real = valor_aumento - (valor_aumento * (inflacao / 100))
    
    
    print(f"Salário antes do reajuste: R$ {salario_atual:.2f}")
    print(f"Percentual de aumento aplicado: {percentual_aumento}%")
    print(f"Valor do aumento: R$ {valor_aumento:.2f}")
    print(f"Novo salário, após o aumento: R$ {novo_salario:.2f}")
    print(f"Valor do aumento real, descontado a inflação: R$ {valor_aumento_real:.2f}")


salario_atual = float(input("Digite o salário atual do colaborador: "))
calcular_reajuste(salario_atual)
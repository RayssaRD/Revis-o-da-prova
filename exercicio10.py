'''10.	O custo ao consumidor de um carro novo é a soma do custo de fábrica, da comissão do distribuidor e dos impostos. A comissão e os impostos são calculados sobre o custo de fábrica, conforme a tabela abaixo. Leia o custo de fábrica e escreva o custo ao consumidor.'''


# Lê o custo de fábrica
custo_fabrica = float(input("Digite o custo de fábrica do carro: R$ "))

# Inicializa variáveis
percentual_distribuidor = 0
percentual_impostos = 0

# Define as porcentagens conforme a tabela
if custo_fabrica <= 12000:
    percentual_distribuidor = 5
    percentual_impostos = 0
elif custo_fabrica <= 25000:
    percentual_distribuidor = 10
    percentual_impostos = 15
else:
    percentual_distribuidor = 15
    percentual_impostos = 20

# Calcula os valores
comissao = custo_fabrica * (percentual_distribuidor / 100)
impostos = custo_fabrica * (percentual_impostos / 100)

# Calcula custo final
custo_consumidor = custo_fabrica + comissao + impostos

# Exibe o resultado
print(f"Custo ao consumidor: R$ {custo_consumidor:.2f}")
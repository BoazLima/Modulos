# 4. Importe apenas as funções mean e median do módulo statistics
from statistics import mean, median

# A mesma lista de dados
dados = [10, 12, 15, 18, 20, 22, 25, 28, 30, 32, 35, 38, 40, 42]

# Calcule a média e a mediana diretamente
media = mean(dados)
mediana = median(dados)

print("Importando apenas as funções:")
print("Média:", media)
print("Mediana:", mediana)
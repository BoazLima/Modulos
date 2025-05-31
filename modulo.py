
# 1. Importe o módulo statistics e crie a lista
import statistics

dados = [10, 12, 15, 18, 20, 22, 25, 28, 30, 32, 35, 38, 40, 42]

# 2. Calcule média e mediana usando o módulo completo
media = statistics.mean(dados)
mediana = statistics.median(dados)

print("Usando módulo completo:")
print("Média:", media)
print("Mediana:", mediana)

# 3. Usando alias (apelido) para o módulo
import statistics as st

media2 = st.mean(dados)
mediana2 = st.median(dados)

print("Média:", media2)
print("Mediana:", mediana2)
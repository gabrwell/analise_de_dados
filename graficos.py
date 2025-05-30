import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# Carregar o conjunto de dados (assumindo que está salvo como CSV)
# Se for um arquivo Excel, substitua por: df = pd.read_excel('flood_risk_dataset_india 11.xlsx')
df = pd.read_excel('flood_risk_dataset_india 11.xlsx')

# Gráfico 1: Gráfico de Barras para Inundações Históricas (Variável Discreta)
plt.figure(figsize=(8, 6))
hist_floods_freq = df['Historical Floods'].value_counts().sort_index()
plt.bar(hist_floods_freq.index, hist_floods_freq.values, color='#1f77b4', edgecolor='black')
plt.title('Distribuição de Inundações Históricas', fontsize=14, pad=15)
plt.xlabel('Inundações Históricas (0 = Não, 1 = Sim)', fontsize=12)
plt.ylabel('Frequência', fontsize=12)
plt.xticks([0, 1], ['Não', 'Sim'])
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()

# Gráfico 2: Histograma para Precipitação (mm) (Variável Contínua)
plt.figure(figsize=(8, 6))
plt.hist(df['Rainfall (mm)'], bins=int(1 + np.log2(len(df['Rainfall (mm)']))),
         color='#ff7f0e', edgecolor='black')
plt.title('Distribuição de Precipitação (mm)', fontsize=14, pad=15)
plt.xlabel('Precipitação (mm)', fontsize=12)
plt.ylabel('Frequência', fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()

# Exibir os gráficos
plt.show()
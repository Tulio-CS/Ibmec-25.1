import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Gerar dados fictícios
np.random.seed(42)
months = pd.date_range('2024-01-01', '2024-12-31', freq='W')

# Demanda histórica (simulando uma tendência de crescimento com flutuação aleatória)
demanda = 100 + (np.linspace(0, 1000, len(months))) + np.random.normal(0, 200, len(months))

# Preço de venda (variando de forma aleatória em torno de um preço base)
preco_venda = 1500 + np.random.normal(0, 50, len(months))

# Preço de venda da concorrência (ligado ao preço de venda, mas com uma variação diferente)
preco_concorrencia = 1500 + np.random.normal(0, 70, len(months))

# Sazonalidade (acrescentando picos de demanda durante períodos específicos)
sazonalidade = np.sin(np.linspace(0, 2 * np.pi, len(months))) * 500
demanda += sazonalidade

# Perfil do cliente (simulando segmentos de clientes em diferentes proporções)
perfil_cliente = np.random.choice(['Jovem', 'Adulto', 'Idoso'], len(months), p=[0.4, 0.5, 0.1])

# Eventos e promoções (simulando eventos promocionais aleatórios durante o ano)
promocoes = np.zeros(len(months))
promocoes[np.random.choice(len(months), size=30, replace=False)] = 1  # 30 eventos promocionais durante o ano

# Criando DataFrame
df = pd.DataFrame({
    'Data': months,
    'Demanda': demanda,
    'Preco_Venda': preco_venda,
    'Preco_Concorrencia': preco_concorrencia,
    'Sazonalidade': sazonalidade,
    'Perfil_Cliente': perfil_cliente,
    'Promocao': promocoes
})

# Gerando gráficos

# 1. Demanda ao longo do tempo
plt.figure(figsize=(10, 6))
plt.plot(df['Data'], df['Demanda'], label='Demanda', color='tab:blue')
plt.title('Demanda ao Longo do Tempo')
plt.xlabel('Data')
plt.ylabel('Demanda')
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()

# 2. Preço de venda vs Preço da concorrência
plt.figure(figsize=(10, 6))
plt.plot(df['Data'], df['Preco_Venda'], label='Preço de Venda', color='tab:orange')
plt.plot(df['Data'], df['Preco_Concorrencia'], label='Preço Concorrência', color='tab:green')
plt.title('Preço de Venda vs Preço da Concorrência')
plt.xlabel('Data')
plt.ylabel('Preço')
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()

# 3. Demanda com Sazonalidade
plt.figure(figsize=(10, 6))
plt.plot(df['Data'], df['Demanda'], label='Demanda Total', color='tab:blue')
plt.plot(df['Data'], df['Sazonalidade'], label='Sazonalidade', color='tab:red', linestyle='--')
plt.title('Demanda e Sazonalidade')
plt.xlabel('Data')
plt.ylabel('Demanda')
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()

# 4. Distribuição de Perfil do Cliente
plt.figure(figsize=(8, 6))
df['Perfil_Cliente'].value_counts().plot(kind='pie', color=['tab:blue', 'tab:orange', 'tab:green'])
plt.title('Distribuição de Perfil do Cliente')
plt.xlabel('Perfil')
plt.ylabel('Quantidade')
plt.xticks(rotation=0)
plt.tight_layout()

# 5. Efeito das Promoções na Demanda
df['Demanda_Apos_Promocao'] = df['Demanda'] + df['Promocao'] * 500
plt.figure(figsize=(10, 6))
plt.plot(df['Data'], df['Demanda'], label='Demanda', color='tab:blue')
plt.plot(df['Data'], df['Demanda_Apos_Promocao'], label='Demanda com Promoção', color='tab:red', linestyle='--')
plt.title('Efeito das Promoções na Demanda')
plt.xlabel('Data')
plt.ylabel('Demanda')
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()

# Exibir gráficos
plt.show()

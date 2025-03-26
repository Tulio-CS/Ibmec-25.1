import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Gerando dados fictícios para o cenário proposto
np.random.seed(42)

# Definindo as variáveis
n = 500  # número de eleitores
idades = np.random.randint(18, 80, size=n)  # idades entre 18 e 80
generos = np.random.choice(['Masculino', 'Feminino'], size=n)  # gênero
regioes = np.random.choice(['Norte', 'Sul', 'Leste', 'Oeste'], size=n)  # regiões
preferencia_candidato = np.random.choice(['Candidato A', 'Candidato B', 'Candidato C'], size=n)  # preferência de voto

# Criando o DataFrame
df = pd.DataFrame({
    'Idade': idades,
    'Gênero': generos,
    'Região': regioes,
    'Preferência': preferencia_candidato
})

# Definindo as variáveis para a rosa dos ventos
regioes_unicas = ['Norte', 'Sul', 'Leste', 'Oeste']

# Contando a distribuição de votos para cada região
votos_norte = df[df['Região'] == 'Norte']['Preferência'].value_counts(normalize=True).reindex(['Candidato A', 'Candidato B', 'Candidato C']).fillna(0)
votos_sul = df[df['Região'] == 'Sul']['Preferência'].value_counts(normalize=True).reindex(['Candidato A', 'Candidato B', 'Candidato C']).fillna(0)
votos_leste = df[df['Região'] == 'Leste']['Preferência'].value_counts(normalize=True).reindex(['Candidato A', 'Candidato B', 'Candidato C']).fillna(0)
votos_oeste = df[df['Região'] == 'Oeste']['Preferência'].value_counts(normalize=True).reindex(['Candidato A', 'Candidato B', 'Candidato C']).fillna(0)

# Organizando os dados para o gráfico
votos = pd.DataFrame({
    'Norte': votos_norte,
    'Sul': votos_sul,
    'Leste': votos_leste,
    'Oeste': votos_oeste
})

# Configurando o gráfico da rosa dos ventos
angles = np.linspace(0, 2 * np.pi, len(regioes_unicas), endpoint=False).tolist()

# Configurando o gráfico polar
fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

# Plotando os votos para cada região
ax.plot(angles, votos['Norte'], color='#66c2a5', label='Candidato A', linewidth=2)
ax.fill(angles, votos['Norte'], color='#66c2a5', alpha=0.25)

ax.plot(angles, votos['Sul'], color='#fc8d62', label='Candidato B', linewidth=2)
ax.fill(angles, votos['Sul'], color='#fc8d62', alpha=0.25)

ax.plot(angles, votos['Leste'], color='#8da0cb', label='Candidato C', linewidth=2)
ax.fill(angles, votos['Leste'], color='#8da0cb', alpha=0.25)

ax.plot(angles, votos['Oeste'], color='#e78ac3', label='Candidato A', linewidth=2)  # Região Oeste
ax.fill(angles, votos['Oeste'], color='#e78ac3', alpha=0.25)  # Região Oeste

# Removendo as marcas do eixo radial
ax.set_yticklabels([])

# Definindo as regiões nas direções corretas
ax.set_xticks(angles)
ax.set_xticklabels(regioes_unicas, fontsize=12)

# Título e legenda
ax.set_title("Distribuição de Voto por Região (Rosa dos Ventos)", size=16, pad=20)
ax.legend(loc='upper left', bbox_to_anchor=(1.2, 1))

# Exibindo o gráfico
plt.show()

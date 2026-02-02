import os
import pandas as pd
import matplotlib.pyplot as plt
from dados import carregar_dados

df = carregar_dados()
df['Data'] = pd.to_datetime(df['Data'])
df['Valor'] = pd.to_numeric(df['Valor'], errors='coerce').fillna(0)

seasons = {
    'Verão': ('2025-01-01', '2025-03-20'),
    'Outono': ('2025-03-21', '2025-06-20'),
    'Inverno': ('2025-06-21', '2025-09-22'),
    'Primavera': ('2025-09-23', '2025-12-31')
}

labels, somas, medias = [], [], []

for nome, (inicio, fim) in seasons.items():
    filtro = df[(df['Data'] >= inicio) & (df['Data'] <= fim)]
    labels.append(nome)
    somas.append(filtro['Valor'].sum())
    medias.append(filtro['Valor'].mean() if not filtro.empty else 0)

def func_format(pct, allvals):
    absolute = pct/100.*sum(allvals)
    return f"{pct:.1f}%\n({absolute:.1f} mm)"

cores = ['#ffcc5c', '#ff6f61', '#88d8b0', '#92a8d1']
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 8))

wedges1, texts1, autotexts1 = ax1.pie(
    somas, labels=labels, 
    autopct=lambda pct: func_format(pct, somas),
    startangle=140, colors=cores, explode=(0.05, 0.05, 0.05, 0.05)
)
ax1.set_title('Precipitação Total por Estação', fontsize=15, fontweight='bold')

wedges2, texts2, autotexts2 = ax2.pie(
    medias, labels=labels, 
    autopct=lambda pct: func_format(pct, medias),
    startangle=140, colors=cores, explode=(0.05, 0.05, 0.05, 0.05)
)
ax2.set_title('Média Diária por Estação', fontsize=15, fontweight='bold')

plt.setp(autotexts1, size=10, weight="bold", color="black")
plt.setp(autotexts2, size=10, weight="bold", color="black")

plt.tight_layout()

diretorio_atual = os.path.dirname(__file__)
pasta_destino = os.path.join(diretorio_atual, 'graficos')
if not os.path.exists(pasta_destino):
    os.makedirs(pasta_destino)

plt.savefig(os.path.join(pasta_destino, 'pizza_estacoes.png'), dpi=300)
plt.show()
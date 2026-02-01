import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import calendar
import locale
from dados import carregar_dados

try:
    locale.setlocale(locale.LC_TIME, 'pt_BR.utf-8')
except:
    pass

df = carregar_dados()

df_mensal = df.groupby(df['Data'].dt.month).agg({'Valor': 'sum'}).reset_index()
df_mensal['Mes_Nome'] = df_mensal['Data'].apply(lambda x: calendar.month_name[x].capitalize())

media_mensal = df_mensal['Valor'].mean()

sns.set_theme(style="darkgrid")
fig, ax = plt.subplots(figsize=(12, 6))

sns.barplot(data=df_mensal, x='Mes_Nome', y='Valor', palette='viridis', ax=ax)

ax.axhline(media_mensal, color='red', linestyle='--', linewidth=2, label=f'Média: {media_mensal:.2f}mm')

for p in ax.patches:
    ax.annotate(f'{p.get_height():.1f}', 
                (p.get_x() + p.get_width() / 2., p.get_height()), 
                ha = 'center', va = 'center', 
                xytext = (0, 9), 
                textcoords = 'offset points',
                fontsize=10, fontweight='bold')

plt.title('Precipitação Total Mensal - 2025', fontsize=16, fontweight='bold')
plt.xlabel('Mês', fontsize=12)
plt.ylabel('Precipitação Total (mm)', fontsize=12)
plt.legend()

diretorio_atual = os.path.dirname(__file__)
pasta_destino = os.path.join(diretorio_atual, 'graficos')

if not os.path.exists(pasta_destino):
    os.makedirs(pasta_destino)

caminho_salvamento = os.path.join(pasta_destino, 'media_mensal.png')

plt.tight_layout()
plt.savefig(caminho_salvamento, dpi=300)
plt.show()
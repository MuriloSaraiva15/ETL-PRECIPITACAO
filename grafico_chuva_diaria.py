import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from dados import carregar_dados


df = carregar_dados()

df['Data'] = pd.to_datetime(df['Data'])
df['Valor'] = pd.to_numeric(df['Valor'], errors='coerce').fillna(0)
df = df.sort_values('Data')

df_somente_chuva = df[df['Valor'] > 0]
dias_com_chuva_real = df_somente_chuva.groupby(df_somente_chuva['Data'].dt.date)['Valor'].sum()
media_dias_chuvosos = dias_com_chuva_real.mean()

media_chuva_por_dia = df['Valor'].mean()

sns.set_theme(style="darkgrid")
fig, ax = plt.subplots(figsize=(15, 6))

sns.lineplot(data=df, x='Data', y='Valor', color='#5DADE2', linewidth=1.5)

sns.scatterplot(data=df[df['Valor'] > 0], x='Data', y='Valor', color='#E67E22', s=20, label='Dias com Chuva')

plt.axhline(media_chuva_por_dia, color='#C0392B', linestyle='--', linewidth=2, label=f'Média Diária: {media_chuva_por_dia:.2f}mm')

plt.axhline(media_dias_chuvosos, color='#8E44AD', linestyle='--', linewidth=2, label=f'Média somente dos dias com chuvas: {media_dias_chuvosos:.2f}mm')

ax.xaxis.set_major_locator(mdates.MonthLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter('%B'))

plt.title('Precipitação Diária - 2025', fontsize=16, fontweight='bold')
plt.xlabel('Tempo', fontsize=12)
plt.ylabel('Chuva (mm)', fontsize=12)
plt.legend()

plt.gcf().autofmt_xdate()

diretorio_atual = os.path.dirname(__file__)
pasta_destino = os.path.join(diretorio_atual, 'graficos')
if not os.path.exists(pasta_destino):
    os.makedirs(pasta_destino)

caminho_salvamento = os.path.join(pasta_destino, 'precipitacao_diaria.png')
plt.tight_layout()
plt.savefig(caminho_salvamento, dpi=300)
plt.show()
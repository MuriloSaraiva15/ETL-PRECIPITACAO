import pandas as pd
import calendar

df = pd.read_csv("dados-precipitacao.csv", delimiter=",", decimal=",")

print(df.head)
print(df.info())



# Removendo colunas e a primeira linha
df = df.iloc[1:].drop(columns=['Prefixo', 'Nome', 'TipoPosto', 'Valor2'])



# Transformando colunas para date e float
df['Data'] = pd.to_datetime(df['Data'])
df['Valor'] = pd.to_numeric(df['Valor'], errors='coerce')

print(df.info())



# Procurar valores duplicados
print(f'O número de valores duplicados: {df.duplicated().sum()}')



# Procurando linhas com string vazias'
print(f'O número de linhas vazias: {df.apply(lambda x: x.astype(str).str.strip() == '').sum()}')




# Dias sem registro
dias_registrados = df['Data'].dt.date.nunique()
total_dias_ano = 365
dias_faltantes = total_dias_ano - dias_registrados

print(f'Dias sem registro: {dias_faltantes}')



# Dias registrados
dias_contados = df['Data'].dt.date.nunique()

print(f'Dias registrados: {dias_contados}')



# Chuva acumulado no ano
chuva_acumulada = df['Valor'].sum().round(2)

print(f'Chuva acumulada no ano de 2025: {chuva_acumulada}mm')



# Precipitação diária média levando em conta todos os dias registrados
chuva_por_dia = chuva_acumulada.mean()

print(f'Precipitação média em relação ao total do ano: {(chuva_por_dia / dias_contados).round(2)}mm')



# Precipitação diária média levando em conta todos os dias que choveram
df_somente_chuva = df[df['Valor'] > 0]
dias_com_chuva_real = df_somente_chuva.groupby(df_somente_chuva['Data'].dt.date)['Valor'].sum()
media_dias_chuvosos = dias_com_chuva_real.mean()

print(f'Em 2025, choveu em média {media_dias_chuvosos:.2f} mm³ nos dias em que houve precipitação.')
print(f'Total de dias com chuva registrados: {len(dias_com_chuva_real)}')



# dias com mais chuvas
top_10_mais_chuva = df.nlargest(10, 'Valor').round(2)
print(f'-----Top 10 dias com mais chuva em 2025-----')
for index, linha in top_10_mais_chuva.iterrows():
    data_formatada = linha['Data'].strftime('%d/%m/%Y')
    print(f'{data_formatada}: {linha['Valor']}mm')



# dia com menos chuva
top_10_menos_chuva = df[df['Valor'] > 0].nsmallest(10, 'Valor').round(2)
print(f'-----Top 10 dias com menos chuva em 2025-----')
for index, linha in top_10_menos_chuva.iterrows():
    data_formatada = linha['Data'].strftime('%d/%m/%Y')
    print(f"{data_formatada}: {linha['Valor']}mm")



# dias sem chuva
print(f'Dias sem chuva: {df.Valor[df.Valor == 0].count()}')



# chuva por semana
print(f'Quantidade de chuva em cada de semana do ano em mm')
chuva_semanal = df.set_index('Data')['Valor'].resample('W').sum().round(2)
renomear_semanas = [f"{i+1}ª Semana" for i in range(len(chuva_semanal))]
chuva_semanal.index = renomear_semanas
print(chuva_semanal)



# precipitação mensal
print(f'Acumulado de chuva ao mês em mm')
total_mes = df.groupby(df['Data'].dt.month)['Valor'].sum().round(2)
total_mes.index = total_mes.index.map(lambda x: calendar.month_name[x])

print(total_mes)



# precipitação media mensal
chuva_por_mes = df.groupby(df['Data'].dt.month)['Valor'].sum()
media_mensal = chuva_por_mes.mean()

print(f"A média mensal de precipitação é: {media_mensal:.2f}")



# chuva no verao
inicio_verao = '01-01-2025'
fim_verao = '20-03-2025'
verao = df[(df['Data'] >= inicio_verao) & (df['Data'] <= fim_verao)]
soma_verao = verao['Valor'].sum()
media_verao = verao['Valor'].mean()

print(f"Soma do verao: {soma_verao:.2f}mm")
print(f"Média do verao: {media_verao:.2f}mm")



# chuva no outono
inicio_outono = '20-03-2025'
fim_outono = '20-06-2025'
outono = df[(df['Data'] >= inicio_outono) & (df['Data'] <= fim_outono)]
soma_outono = outono['Valor'].sum()
media_outono = outono['Valor'].mean()

print(f"Soma do outono: {soma_outono:.2f}mm")
print(f"Média do outono: {media_outono:.2f}mm")



# chuva no inverno
inicio_inverno = '20-06-2025'
fim_inverno = '22-09-2025'
inverno = df[(df['Data'] >= inicio_inverno) & (df['Data'] <= fim_inverno)]
soma_inverno = inverno['Valor'].sum()
media_inverno = inverno['Valor'].mean()

print(f"Soma do inverno: {soma_inverno:.2f}mm")
print(f"Média do inverno: {media_inverno:.2f}mm")



# chuva na primavera
inicio_primavera = '22-09-2025'
fim_primavera = '31-12-2025'
primavera = df[(df['Data'] >= inicio_primavera) & (df['Data'] <= fim_primavera)]
soma_primavera = primavera['Valor'].sum()
media_primavera = primavera['Valor'].mean()

print(f"Soma do primavera: {soma_primavera:.2f}mm")
print(f"Média do primavera: {media_primavera:.2f}mm")



def carregar_dados():
    df = pd.read_csv("dados-precipitacao.csv", delimiter=",", decimal=",")
    df = df.iloc[1:].drop(columns=['Prefixo', 'Nome', 'TipoPosto', 'Valor2'])
    df['Data'] = pd.to_datetime(df['Data'])
    df['Valor'] = pd.to_numeric(df['Valor'], errors='coerce')
    return df

if __name__ == '__main__':
    dados = carregar_dados()
    
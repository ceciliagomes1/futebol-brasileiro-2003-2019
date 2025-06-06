import pandas as pd
import os

entrada = '/content/matches-2003-2019.txt'
saida = '/content/matches-2003-2019.csv'

df = pd.read_csv(entrada, sep=';', encoding='latin1')

df.columns = [col.lower().replace(" ", "_").replace("-", "_").replace("#", "") for col in df.columns]

print(df.head())
print(df.columns)

print("\nDados ausentes por coluna")
print(df.isnull().sum())

df[['gols_mandante', 'gols_visitante']] = df['score'].str.extract(r'(\d+)x(\d+)')
df['gols_mandante'] = df['gols_mandante'].astype(float)
df['gols_visitante'] = df['gols_visitante'].astype(float)

df = df.drop(columns=['score'])

os.makedirs(os.path.dirname(saida), exist_ok=True)
df.to_csv(saida, index=False)
print(f"Arquivo tratado com sucesso em: {saida}")

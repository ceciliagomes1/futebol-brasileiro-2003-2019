import seaborn as sns
import matplotlib.pyplot as plt

df['date'] = pd.to_datetime(df['date'], dayfirst=True)
df['ano'] = df['date'].dt.year
df['total_gols'] = df['gols_mandante'] + df['gols_visitante']

gols_por_ano = df.groupby('ano')['total_gols'].sum()

plt.figure(figsize=(10,5))
sns.barplot(x=gols_por_ano.index, y=gols_por_ano.values, color='darkgreen')
plt.title('Total de Gols por Ano no Campeonato Brasileiro / 2003-2019', color='darkblue')
plt.xlabel('Ano', size=15)
plt.ylabel('Gols',size=15)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

---

df['vencedor'] = df.apply(
    lambda row: row['home_team'] if row['gols_mandante'] > row['gols_visitante'] 
    else row['away_team'] if row['gols_visitante'] > row['gols_mandante'] 
    else 'empate', axis=1)

vitorias = df[df['vencedor'] != 'empate']['vencedor'].value_counts().head(10)

plt.figure(figsize=(10,5))
sns.barplot(x=vitorias.values, y=vitorias.index, color='gray')
plt.title('Top 10 Times com Mais Vitórias (2003-2019)')
plt.xlabel('Vitórias')
plt.ylabel('Times')
plt.tight_layout()
plt.show()

---

media_gols = df['total_gols'].mean()
print(f'Média de gols por jogo: {media_gols:.2f}')


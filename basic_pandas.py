import pandas as pd

# Criando um DataFrame a partir de um dicionário
data = {'Nome': ['Alice', 'Bob', 'Charlie'],
        'Idade': [25, 30, 35]}
df = pd.DataFrame(data)

# # Exibindo o DataFrame
# print(df)

# Adicionando uma nova coluna
df['Cidade'] = ['A', 'B', 'C']


# # Exibindo as primeiras linhas
# print(df.head())

# # Informações sobre o DataFrame
# print(df.info())

# # Estatísticas descritivas
# print(df.describe())



# # Filtros
subset = df[df['Idade'] > 30]
# print(subset)


# Agrupamento e agregação


# Excluindo temporariamente a coluna 'Nome'
df_temp = df.drop('Nome', axis=1)

grouped = df_temp.groupby('Cidade').mean()
print(grouped)



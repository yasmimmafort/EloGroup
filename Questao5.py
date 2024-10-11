'''Desenvolva um código em python para buscar o cargo que tem os salários mais altos na companhia, baseando-se nas duas tabelas que estão abaixo.'''

import pandas as pd


dados_trabalhadores = {
    'ID_Trabalhador': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
    'Salario': [100000, 80000, 300000, 500000, 500000, 200000, 75000, 90000, 90000, 65000, 75000, 85000]
}

dados_cargos = {
    'ID_Ref_Trabalhador': [1, 2, 3, 5, 4, 7, 6],
    'Cargo': ['Gerente', 'Executivo', 'Executivo', 'Gerente', 'Gerente Associado', 'Gerente de projetos', 'Líder']
}


df_trabalhadores = pd.DataFrame(dados_trabalhadores)
df_cargos = pd.DataFrame(dados_cargos)


df_juncao = pd.merge(df_trabalhadores, df_cargos, left_on='ID_Trabalhador', right_on='ID_Ref_Trabalhador', how='left')
df_juncao['Cargo'] = df_juncao['Cargo'].fillna("Sem Cargo")

salario_por_cargo = df_juncao.groupby('Cargo')['Salario'].max().reset_index()
cargo_mais_alto = salario_por_cargo[salario_por_cargo['Salario'] == salario_por_cargo['Salario'].max()]

print(df_trabalhadores, "\n")
print(df_cargos, "\n")
print(df_juncao, "\n")
print("Cargo com o maior salário:\n", cargo_mais_alto)

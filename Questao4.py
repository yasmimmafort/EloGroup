'''Desenvolva um codigo python para encontrar todos os usuarios que estao ativos por tres dias'''

import pandas as pd

dados = {
    'Data': ['2020-12-06', '2021-01-15', '2021-01-06', '2021-01-02', '2020-12-24', 
             '2020-12-08', '2020-12-09', '2021-01-11', '2021-01-10', '2021-01-12',
             '2021-01-15', '2021-01-15', '2020-12-17', '2020-12-25', '2020-12-25', 
             '2020-12-06', '2021-01-01', '2021-01-14', '2021-02-07', '2021-02-10',
             '2021-02-01', '2021-02-01', '2021-02-01'],
    'ID_Usuario': ['U1', 'U2', 'U3', 'U1', 'U2', 'U1', 'U1', 'U4', 'U4', 'U4', 
                   'U2', 'U4', 'U5', 'U6', 'U5', 'U7', 'U6', 'U6', 'U4', 'U2', 
                   'U4', 'U4', 'U5']
}

df = pd.DataFrame(dados)
df['Data'] = pd.to_datetime(df['Data'])
df = df.sort_values(by=['ID_Usuario', 'Data']).drop_duplicates()

dias_consecutivos = 0

def logins_consecutivos(df, dias_consecutivos):
    usuarios_consecutivos = []
    for usuario, grupo in df.groupby('ID_Usuario'):
        if any(grupo['Data'].diff().dt.days[1:].rolling(dias_consecutivos - 1).sum() == dias_consecutivos - 1):
            usuarios_consecutivos.append(usuario)
    return usuarios_consecutivos

if dias_consecutivos < 1:
    print("Nenhum usuário ativo por 0 dias consecutivos.")
else:
    usuarios_consecutivos = logins_consecutivos(df, dias_consecutivos)
    print(f"Usuários ativos por {dias_consecutivos} dias consecutivos:", usuarios_consecutivos)
    
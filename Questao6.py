'''Desenvolva um código em python para comparar as taxas de retenção em janeiro de 2023 com as de dezembro de 2022. 
A taxa de retenção é definida como a porcentagem de colaboradores que uma empresa retém durante um determinado período de tempo, 
baseando-se na tabela ao lado. 
Quais account_id tiveram a maior taxa de retenção?'''


import pandas as pd

dados = {
    'Data': ['01/01/2023 00:00', '01/01/2023 00:00', '06/01/2023 00:00', '06/01/2023 00:00',
             '24/12/2022 00:00', '08/12/2022 00:00', '09/12/2022 00:00', '11/01/2023 00:00', 
             '06/01/2023 00:00', '15/01/2023 00:00', '10/01/2023 00:00', '11/12/2022 00:00',
             '25/12/2022 00:00', '25/12/2022 00:00', '05/12/2022 00:00', '05/12/2022 00:00',
             '01/01/2023 00:00', '14/01/2023 00:00', '07/02/2023 00:00', '10/02/2023 00:00', 
             '05/12/2022 00:00', '01/01/2023 00:00', '05/12/2022 00:00'],
    'ID_Conta': ['A1', 'A1', 'A1', 'A1', 'A1', 'A1', 'A1', 'A2', 'A2', 'A2', 'A2', 'A2',
                   'A2', 'A2', 'A3', 'A3', 'A3', 'A3', 'A4', 'A4', 'A1', 'A2', 'A1'],
    'ID_Usuario': ['USER1', 'USER2', 'USER3', 'USER1', 'USER1', 'USER1', 'USER2', 'USER4', 'USER4', 
                'USER5', 'USER5', 'USER4', 'USER5', 'USER6', 'USER7', 'USER6', 'USER6', 
                'USER6', 'USER2', 'USER4', 'USER8', 'USER5', 'USER8']
}

df = pd.DataFrame(dados)

df['Data'] = pd.to_datetime(df['Data'], format='%d/%m/%Y %H:%M')

dez_2022 = df[(df['Data'].dt.month == 12) & (df['Data'].dt.year == 2022)]
jan_2023 = df[(df['Data'].dt.month == 1) & (df['Data'].dt.year == 2023)]

retencao = {}

for account in df['ID_Conta'].unique():
    usuarios_dez = set(dez_2022[dez_2022['ID_Conta'] == account]['ID_Usuario'])
    usuarios_jan = set(jan_2023[jan_2023['ID_Conta'] == account]['ID_Usuario'])
    
    if len(usuarios_dez) > 0:
        taxa_retenção = len(usuarios_jan.intersection(usuarios_dez)) / len(usuarios_dez) * 100
        retencao[account] = taxa_retenção


maior_retenção = max(retencao, key=retencao.get)
print(f"Taxa de retenção por ID_Conta: {retencao}")

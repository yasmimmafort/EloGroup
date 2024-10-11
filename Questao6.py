import pandas as pd

dados = {
    'Data': ['01/01/2023 00:00', '01/01/2023 00:00', '06/01/2023 00:00', '06/01/2023 00:00',
             '24/12/2022 00:00', '08/12/2022 00:00', '09/12/2022 00:00', '11/01/2023 00:00', 
             '06/01/2023 00:00', '15/01/2023 00:00', '10/01/2023 00:00', '11/12/2022 00:00',
             '25/12/2022 00:00', '25/12/2022 00:00', '05/12/2022 00:00', '05/12/2022 00:00',
             '01/01/2023 00:00', '14/01/2023 00:00', '07/02/2023 00:00', '10/02/2023 00:00', 
             '05/12/2022 00:00', '01/01/2023 00:00', '05/12/2022 00:00', '15/07/2021 00:00', 
             '20/08/2021 00:00', '15/09/2021 00:00', '10/10/2021 00:00', '05/11/2021 00:00',
             '01/12/2021 00:00', '15/12/2021 00:00', '20/01/2022 00:00', '25/02/2022 00:00', 
             '15/03/2022 00:00', '30/04/2022 00:00', '05/05/2022 00:00', '15/06/2022 00:00',
             '01/01/2023 00:00', '01/01/2023 00:00', '24/12/2022 00:00', '11/01/2023 00:00', 
             '15/07/2021 00:00', '20/08/2021 00:00', '25/02/2022 00:00', '10/01/2023 00:00',
             '05/11/2021 00:00', '01/12/2021 00:00', '15/12/2021 00:00', '20/01/2022 00:00', 
             '30/04/2022 00:00', '05/05/2022 00:00', '01/01/2023 00:00', '06/01/2023 00:00',
             '24/12/2022 00:00', '08/12/2022 00:00', '15/07/2021 00:00', '11/01/2023 00:00', 
             '10/02/2023 00:00', '05/12/2022 00:00', '14/01/2023 00:00', '07/02/2023 00:00'],
    'ID_Conta': ['A1', 'A1', 'A1', 'A1', 'A1', 'A1', 'A1', 'A2', 'A2', 'A2', 'A2', 'A2',
                 'A2', 'A2', 'A3', 'A3', 'A3', 'A3', 'A4', 'A4', 'A1', 'A2', 'A1', 'A5', 
                 'A5', 'A5', 'A5', 'A5', 'A5', 'A5', 'A6', 'A6', 'A6', 'A6', 'A6', 'A6',
                 'A1', 'A1', 'A1', 'A2', 'A5', 'A5', 'A5', 'A2', 'A1', 'A1', 'A1', 'A1', 
                 'A2', 'A2', 'A1', 'A1', 'A2', 'A2', 'A5', 'A2', 'A2', 'A1', 'A2', 'A2'],
    'ID_Usuario': ['USER1', 'USER2', 'USER3', 'USER1', 'USER1', 'USER1', 'USER2', 'USER4', 'USER4', 
                   'USER5', 'USER5', 'USER4', 'USER5', 'USER6', 'USER7', 'USER6', 'USER6', 
                   'USER6', 'USER2', 'USER4', 'USER8', 'USER5', 'USER8', 'USER9', 'USER9', 
                   'USER10', 'USER11', 'USER12', 'USER13', 'USER9', 'USER10', 'USER14', 
                   'USER15', 'USER10', 'USER12', 'USER13', 'USER1', 'USER2', 'USER1', 'USER4', 
                   'USER9', 'USER9', 'USER10', 'USER5', 'USER1', 'USER2', 'USER3', 'USER1', 
                   'USER5', 'USER6', 'USER1', 'USER2', 'USER4', 'USER4', 'USER9', 'USER5', 
                   'USER4', 'USER1', 'USER5', 'USER4']
}
df = pd.DataFrame(dados)
df['Data'] = pd.to_datetime(df['Data'], format='%d/%m/%Y %H:%M')


def calcular_taxa_retenção(df, inicio_1, fim_1, inicio_2, fim_2):
    periodo_1 = df[(df['Data'] >= inicio_1) & (df['Data'] <= fim_1)]
    periodo_2 = df[(df['Data'] >= inicio_2) & (df['Data'] <= fim_2)]
    retencao = {}

    for conta in df['ID_Conta'].unique():
        usuarios_1 = set(periodo_1[periodo_1['ID_Conta'] == conta]['ID_Usuario'])
        usuarios_2 = set(periodo_2[periodo_2['ID_Conta'] == conta]['ID_Usuario'])
        if usuarios_1:
            retencao[conta] = len(usuarios_2 & usuarios_1) / len(usuarios_1) * 100
    
    return retencao

#teste 1
print("Retenção de Julho-Dezembro 2021 para Janeiro-Junho 2022:", 
      calcular_taxa_retenção(df, '2021-07-01', '2021-12-31', '2022-01-01', '2022-06-30'))
#teste2
print("Retenção de Janeiro-Março 2022 para Outubro-Dezembro 2022:", 
      calcular_taxa_retenção(df, '2022-01-01', '2022-03-31', '2022-10-01', '2022-12-31'))
#teste3
print("Retenção de Dezembro 2022 para Janeiro 2023:", 
      calcular_taxa_retenção(df, '2022-12-01', '2022-12-31', '2023-01-01', '2023-01-31'))

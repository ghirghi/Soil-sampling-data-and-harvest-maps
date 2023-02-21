# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sklearn
from IPython.display import display
from shapely.geometry import Point, Polygon
import geopandas as gpd
pd.set_option('mode.chained_assignment', None)

usuario = 'josue'
#Josué

rawdata = pd.DataFrame(pd.read_csv(fr'C:\Users\{usuario}\OneDrive\Dados Agua Clara 1\2023\Taxa variavel safrinha 1S 2023\vetor_Unido_colheita_analises_p12.csv', index_col=None))
analises = pd.DataFrame(pd.read_excel(fr'C:\Users\{usuario}\OneDrive\Dados Agua Clara 1\2023\Taxa variavel safrinha 1S 2023\Amostras de solo 2022 areas safrinha.xlsx', sheet_name='Sheet1',index_col=None))

colheitap12 = pd.DataFrame(pd.read_csv(fr'C:\Users\{usuario}\OneDrive\Dados Agua Clara 1\2023\Taxa variavel safrinha 1S 2023\grade_com_massa_e_nutrientes.csv', index_col=None))
vetor_colP12 = pd.DataFrame(pd.read_csv(fr'C:\Users\{usuario}\OneDrive\Dados Agua Clara 1\2023\Taxa variavel safrinha 1S 2023\teste_vetor_p12.csv', index_col=None))

#colhido liquido = 254.854,80
#tem que ajustar o valor da massa se não vai dar erro

colheitap12['colhido'] = colheitap12['massa'] * (colheitap12['area'])

vetor_colP12['colhido'] = vetor_colP12['massa'] * (vetor_colP12['area'])

vetor_colP12

print('grid', colheitap12['colhido'].sum())
print('vetor',vetor_colP12['colhido'].sum())

colheitap12['massa corrigida'] = colheitap12['massa'] / 0.5107
colheitap12['colhido corrigido'] = colheitap12['massa corrigida'] * (colheitap12['area'])
print('grid', colheitap12['colhido corrigido'].sum())

vetor_colP12['massa corrigida'] = vetor_colP12['massa'] / 0.8560
vetor_colP12['colhido corrigido'] = vetor_colP12['massa'] * vetor_colP12['area']
print('vetor', vetor_colP12['colhido corrigido'].sum())
# %%
colheitap12 = vetor_colP12
adubo_fosforo = 0.34
colheitap12['recomendação'] = ''

contador = 0

adubo_fosforo = 0.34

def condicoes_fosforo(fosforo, massa):
    if massa <= 2:
        if fosforo < 0.6:
            return 60
        elif 0.6 < fosforo <= 7:
            return 40
        elif 7 < fosforo < 15:
            return 30
        else:
            return 20
    elif 2 < massa <= 4:
        if fosforo < 0.6:
            return 80
        elif 0.6 < fosforo <= 7:
            return 60
        elif 7 < fosforo < 15:
            return 40
        else:
            return 30
    elif 4 < massa <= 6:
        if fosforo < 0.6:
            return 80
        elif 0.6 < fosforo <= 7:
            return 60
        elif 7 < fosforo < 15:
            return 40
        else:
            return 30
    elif 6 < massa <= 8:
        if fosforo < 0.6:
            return 90
        elif 0.6 < fosforo <= 7:
            return 70
        elif 7 < fosforo < 15:
            return 50
        else:
            return 30
    elif 8 < massa <= 10:
        if fosforo < 0.6:
            return 90
        elif 0.6 < fosforo <= 7:
            return 90
        elif 7 < fosforo < 15:
            return 60
        else:
            return 40
    else:
        if fosforo < 0.6:
            return 100
        elif 0.6 < fosforo <= 7:
            return 100
        elif 7 < fosforo < 15:
            return 70
        else:
            return 50

colheitap12['recomendação'] = colheitap12.apply(lambda row: condicoes_fosforo(row['P'], row['massa corrigida']), axis=1)
colheitap12['recomendação'] = colheitap12['recomendação'] / adubo_fosforo

colheitap12.to_csv(fr'C:\Users\{usuario}\OneDrive\Dados Agua Clara 1\2023\Taxa variavel safrinha 1S 2023\teste_vetor.csv')

colheitap12

# %%

colheitap12['total adubo'] = colheitap12['recomendação'] * ((colheitap12['area']) / 1000)
colheitap12.groupby('massa corrigida')['recomendação', 'P'].mean().reset_index().plot(y = ['recomendação', 'P'], x = 'massa corrigida', title = '\n Totais de adubo',kind="bar", figsize=(9, 8))
colheitap12.groupby('CODE')['massa', 'massa corrigida'].mean().reset_index().plot(y = ['massa', 'massa corrigida'], x = 'CODE', title = '\n Colheita',kind="bar", figsize=(9, 8))
colheitap12.groupby('CODE')[ 'total adubo'].sum().reset_index().plot(y = [ 'total adubo'], x = 'CODE', title = '\n Totais de adubo',kind="bar", figsize=(9, 8))
# %%
colheitap12.groupby('CODE')[ 'area'].sum().reset_index()


# %%
colheitap12.groupby('CODE')[ 'total adubo', ].sum()
# %%
colheitap12['total adubo'].sum()
# %%
colheitap12[['CODE', 'P','massa corrigida','recomendação',  'total adubo']]
# %%

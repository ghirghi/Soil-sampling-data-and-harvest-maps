#%%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sklearn
from IPython.display import display

usuario = 'josue'
#Josué

rawdata = pd.DataFrame(pd.read_csv(fr'C:\Users\{usuario}\OneDrive\Dados Agua Clara 1\2023\Taxa variavel safrinha 1S 2023\vetor_Unido_colheita_analises_p12.csv', index_col=None))
analises = pd.DataFrame(pd.read_excel(fr'C:\Users\{usuario}\OneDrive\Dados Agua Clara 1\2023\Taxa variavel safrinha 1S 2023\Amostras de solo 2022 areas safrinha.xlsx', sheet_name='Sheet1',index_col=None))

rawdata.columns
data = pd.DataFrame(rawdata[['massa','area','P_mean','K_mean']])
analises.drop([0,1], inplace=True)
analises['Fósforo'] = analises['Fósforo'].astype('float')
safrinha = analises[['-','Gleba antiga', 'Gleba nova','Area', 'Fósforo', 'pH', 'Potássio']]
safrinha['producao'] = 8


safrinha = safrinha.astype({'Fósforo': 'float'})
safrinha = safrinha.astype({'Potássio': 'float'})
cond1 = (safrinha['Fósforo'] <= 0.6)
cond2 = (safrinha['Fósforo'] > 0.6) & (safrinha['Fósforo'] <= 15)
cond3 = (safrinha['Fósforo'] > 15) & (safrinha['Fósforo'] <= 40)
cond4 = (safrinha['Fósforo'] > 40)

formula1 = (safrinha['Fósforo'] * 0)
formula2 = (safrinha['Fósforo'] * 0) + (90 / 0.34)
formula3 = (safrinha['Fósforo'] *0) + (60 / 0.34)
formula4 = (safrinha['Fósforo'] *0) + (40 / 0.34)

# use numpy.select to set new values based on the conditions
safrinha['adubação fosforo'] = np.select([cond1, cond2, cond3, cond4], [formula1, formula2, formula3, formula4], default=0)

safrinha['adubação potássio'] =(50 -  ((safrinha['adubação fosforo'])*0.12)) /0.6
safrinha['Total fósforo'] = safrinha['adubação fosforo'] * safrinha['Area']
safrinha['Total potássio'] = safrinha['adubação potássio'] * safrinha['Area']
safrinha.to_excel(fr'C:\Users\{usuario}\OneDrive\Dados Agua Clara 1\2023\Taxa variavel safrinha 1S 2023\Resultados_1_adubação_safrinha.xlsx')

for i in safrinha['-'].unique():
    safrinha[safrinha['-'] == i].plot(y = ['Total fósforo', 'Total potássio'], x = '-', title = i + '\n Taxas',kind="bar", figsize=(9, 8))



display(safrinha)
safrinha.groupby('-')['Total fósforo', 'Total potássio'].sum().reset_index().plot(y = ['Total fósforo', 'Total potássio'], x = '-', title = '\n Totais de adubo',kind="bar", figsize=(9, 8))
safrinha.groupby('-')['Total fósforo', 'Total potássio'].sum().reset_index()


#%%
safrinha[safrinha['-'] == 'Pivô 12']['Total fósforo'].sum()
# %%

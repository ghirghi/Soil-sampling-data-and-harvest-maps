#%%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import geopandas as gpd

frame_2688 = pd.DataFrame(pd.read_csv(r'C:\Users\Josué\OneDrive\Dados Agua Clara 1\2023\Estatisticas colheitas\Pontos_estranhos\2020_2021_soja_2688_area14.csv'))
def plotagem():
    frame_2688[frame_2688['Timestamp'] > '27/02/2021 10:38:15'].plot(y = 'RawMass', x = 'Timestamp')
    frame_2688[frame_2688['Timestamp'] > '27/02/2021 10:38:15'].plot(y = 'Moisture', x = 'Timestamp')

    frame_2688[frame_2688['Timestamp'] < '27/02/2021 10:38:15'].plot(y = 'RawMass', x = 'Timestamp')
    frame_2688[frame_2688['Timestamp'] < '27/02/2021 10:38:15'].plot(y = 'Moisture', x = 'Timestamp')

frame_2688.plot(y = 'RawMass', x = 'Timestamp')
frame_2688.plot(y = 'Moisture', x = 'Timestamp')


valores_menores = frame_2688[frame_2688['Moisture'] < 15]
valores_maiores = frame_2688[frame_2688['Moisture'] > 15]
valores_maiores_boo = frame_2688['Moisture'] > 15

print('mean smaller',valores_menores['RawMass'].mean())
print('median smaller',valores_menores['RawMass'].median())

print('mean bigger',valores_maiores['RawMass'].mean())
print('median bigger',valores_maiores['RawMass'].median())

frame_2688.plot(y = 'RawMass', x = 'Timestamp')
frame_2688.loc[valores_maiores_boo, 'RawMass'] = frame_2688['RawMass'] / 2.2
frame_2688.plot(y = 'RawMass', x = 'Timestamp')


# %%

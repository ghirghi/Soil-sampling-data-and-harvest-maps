#%%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import geopandas as gpd

frame_6130 = pd.DataFrame(pd.read_csv(r'C:\Users\Josué\OneDrive\Dados Agua Clara 1\2023\Estatisticas colheitas\6130_pontos.csv'))
frame_2688 = pd.DataFrame(pd.read_csv(r'C:\Users\Josué\OneDrive\Dados Agua Clara 1\2023\Estatisticas colheitas\2688_pontos.csv'))

geoframe26 = gpd.GeoDataFrame(frame_2688)

frame_2688.plot(y = 'RawMass', x = 'Timestamp')
frame_6130.plot(y = 'RawMass', x = 'Timestamp')

print(frame_6130['RawMass'].median())
print(frame_2688['RawMass'].median())
#%%

frame_2688.columns
# %%
areas26 = frame_2688['TALHAO'].unique()
areas61 = frame_6130['TALHAO'].unique()

print(areas26)
print(areas61)
# %%
frame_2688.drop(frame_2688[frame_2688['RawMass'] == 0].index, inplace=True)
print(frame_2688[frame_2688['TALHAO'] == areas26[5]].plot(y = 'Moisture', x = 'Timestamp',title=len(frame_2688[frame_2688['TALHAO'] == areas26[5]])))
print(frame_2688[frame_2688['TALHAO'] == areas26[5]].plot(y = 'RawMass', x = 'Timestamp'))

frame_6130.drop(frame_6130[frame_6130['RawMass'] == 0].index, inplace=True)
print(frame_6130[frame_6130['TALHAO'] == areas61[0]].plot(y = 'RawMass', x = 'Timestamp', title=len(frame_6130[frame_6130['TALHAO'] == areas61[0]].shape)))
print(frame_6130[frame_6130['TALHAO'] == areas61[0]].plot(y = 'Moisture', x = 'Timestamp'))

# %%
print(geoframe26, )
# %%

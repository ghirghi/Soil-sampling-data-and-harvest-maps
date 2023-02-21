#%%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import geopandas as gpd

frame_6130 = pd.DataFrame(pd.read_csv(r'C:\Users\Josué\OneDrive\Dados Agua Clara 1\2023\Estatisticas colheitas\Pontos_estranhos\2020_2021_soja_6130_P8P9.csv'))
frame_2688 = pd.DataFrame(pd.read_csv(r'C:\Users\Josué\OneDrive\Dados Agua Clara 1\2023\Estatisticas colheitas\Pontos_estranhos\2020_2021_soja_2688_P8P9.csv'))

frame_6130.plot(x = 'Timestamp', y = 'RawMass')
frame_2688.plot(x = 'Timestamp', y = 'RawMass')
# %%
print(frame_6130['RawMass'].mean())
print(frame_2688['RawMass'].mean())

print(frame_6130['RawMass'].mean() / frame_2688['RawMass'].mean())

# %%
frame_2688['RawMass'] = frame_2688['RawMass'] * 2.4
# %%
frame_6130.plot(x = 'Timestamp', y = 'RawMass')
frame_2688.plot(x = 'Timestamp', y = 'RawMass')

# %%

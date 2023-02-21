#%%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import geopandas as gpd


frame_6130 = pd.DataFrame(pd.read_csv(r'C:\Users\Josué\OneDrive\Dados de máquinas\2023\Processados\Pontos_todas_coheitas\2020\2688P4.csv'))
frame_2688 = pd.DataFrame(pd.read_csv(r'C:\Users\Josué\OneDrive\Dados de máquinas\2023\Processados\Pontos_todas_coheitas\2020\6130P4.csv'))

frame_6130.plot(x = 'Timestamp', y = 'RawMass')
frame_2688.plot(x = 'Timestamp', y = 'RawMass')
# %%
print(frame_6130['RawMass'].mean())
print(frame_6130['RawMass'].median())

print(frame_2688['RawMass'].mean())
print(frame_2688['RawMass'].median())

print(frame_6130['RawMass'].mean() / frame_2688['RawMass'].mean())

# %%
frame_6130['RawMass'] = frame_6130['RawMass'] * (frame_6130['RawMass'].mean() / frame_2688['RawMass'].mean())
# %%
frame_6130.plot(x = 'Timestamp', y = 'RawMass')
frame_2688.plot(x = 'Timestamp', y = 'RawMass')

# %%
print(frame_6130['RawMass'].mean())
print(frame_6130['RawMass'].median())

print(frame_2688['RawMass'].mean())
print(frame_2688['RawMass'].median())

print(frame_6130['RawMass'].mean() / frame_2688['RawMass'].mean())

# %%

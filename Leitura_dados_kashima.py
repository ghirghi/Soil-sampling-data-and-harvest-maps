#%%

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

usuario = 'josue'
#Josué


Harvest22 = pd.DataFrame(pd.read_excel(fr'C:\Users\{usuario}\OneDrive\Dados de máquinas\2023\Não processados\Kashima\ArquivosMyJD\Harvest_2022.xlsx', index_col=None),)
Harvest21 = pd.DataFrame(pd.read_excel(fr'C:\Users\{usuario}\OneDrive\Dados de máquinas\2023\Não processados\Kashima\ArquivosMyJD\Harvest_2021.xlsx', index_col=None),)
Harvest20 = pd.DataFrame(pd.read_excel(fr'C:\Users\{usuario}\OneDrive\Dados de máquinas\2023\Não processados\Kashima\ArquivosMyJD\Harvest_2020.xlsx', index_col=None),)
Harvest18 = pd.DataFrame(pd.read_excel(fr'C:\Users\{usuario}\OneDrive\Dados de máquinas\2023\Não processados\Kashima\ArquivosMyJD\Harvest_2018.xlsx', index_col=None),)
Harvest17 = pd.DataFrame(pd.read_excel(fr'C:\Users\{usuario}\OneDrive\Dados de máquinas\2023\Não processados\Kashima\ArquivosMyJD\Harvest_2017.xlsx', index_col=None),)
Harvest15 = pd.DataFrame(pd.read_excel(fr'C:\Users\{usuario}\OneDrive\Dados de máquinas\2023\Não processados\Kashima\ArquivosMyJD\Harvest_2015.xlsx', index_col=None),)


Harvest22['Clients'].unique()
Harvest22['Farms'].unique()
Harvest22['Fields'].unique()
# %%
dfs = [Harvest22, Harvest21, Harvest20, Harvest18, Harvest17, Harvest15]
final_df = pd.concat([Harvest22, Harvest21, Harvest20, Harvest18, Harvest17, Harvest15], ignore_index=True)

final_df['Fields'].unique()
# %%
freq = pd.DataFrame(final_df.groupby(['Fields']).count() )
freq2 = final_df['Fields'].value_counts()
freq2.to_excel(fr'C:\Users\{usuario}\OneDrive\Dados de máquinas\2023\Não processados\Kashima\ArquivosMyJD\contagem.xlsx')
#freq.columns()
# %%
final_df[final_df['Fields'] == 'pivo2021']
# %%

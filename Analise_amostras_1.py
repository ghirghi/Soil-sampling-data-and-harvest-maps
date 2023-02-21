
#%%

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

usuario = 'josue'

amostras22 = pd.DataFrame(pd.read_excel(fr'C:\Users\{usuario}\OneDrive\Dados Agua Clara 1\2022\Analises de solo 2022.xlsx',sheet_name='0-20', index_col=None),)
amostras22.columns = amostras22.loc[0]

amostras22['Dose/Taxa (T)'].sum()
# %%

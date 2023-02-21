# -*- coding: utf-8 -*-
#%%
"""
Created on Mon Dec 12 09:21:02 2022

@author: Josué

Informações
Os parametros para escolhermos os dados são a area e as datas, valores como l/ha, l total, l aplicado
 com as mesmas datas serão somados.
Datas a partir de 20/07 são sem exact apply.
Nosso objetivo é apresentar a variação de l totais, l por ha aplicado vs planejado,
 hectares aplicados por area em decorrer do tempo.


Passo: criar dataframes com cada area

Fazer um dataframe p/ volume etc...
colunas =  datas
linhas/index = area



"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

frame = pd.DataFrame(pd.read_excel('Application_2022.xlsx', index_col=None),
columns = ['Fields','Last Applied','Area Applied' , 'Rate','Total Applied', 'Target Rate', 'Target Total', 'Speed', 'Work'])
#Application_field_dec2021_dec2022.xlsx
#Applicationdec2021_dec2022.xlsx
#Application_2022.xlsx
frame2 = pd.DataFrame(pd.read_excel('Applicationdec2021_dec2022.xlsx', index_col=2),
columns = ['Fields','Last Applied','Area Applied' , 'Rate','Total Applied', 'Target Rate', 'Target Total', 'Speed'])

print(frame.columns, '\n')
print(frame['Fields'][3])

datas = pd.Series(frame['Last Applied'])

areas = pd.Series(frame['Fields'])

datasunicas = pd.Series(datas.unique())

areasunicas = pd.Series(areas.unique())

dctareas = {}
m = 0
while m < len(areasunicas):
    framebolha = frame[frame['Fields'] == areasunicas[m]]
    dctareas[m] = pd.DataFrame(framebolha)
    m += 1

"""

Filtro 1
enquanto n < as areas listadas: 
    trabalhamos com o dicionario[area n]
    
    Filtro 2
    enquanto n < datas da area n:
        trabalhamos com as datas da area n
        
        Filtro 3
        enquanto n < datas x da area n:
            trabalhamos com as datas x da area n

"""

        
"""
Filtra datas: Como a funcao vai trabalhar?
    Ela recebe o parametro area (n), então busca no dct areas a area. 
    dctareas[n]
    
    Então ela estabelece um filtro com base nas datas do dataframe dessa area
    dctareas[n][dctareas[n]['Last Applied'] == datasunicas[m]]
    Assim temos em retorno um df com as datas m

"""

dctareas2 = {}
def filtradatas(qual_area, qual_data):
    """
    ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    MAPA
    OBJETIVO: somar os parametros de 7 linhas e coloca-los em uma linha.

    1. framebolha2 filtra as datas e areas

    2. SE eu tiver duplicidade de aplicação nas datas associo as duplas em um segundo dct, em um passo de 7(existe um motivo pelo 7)
    2.1 Faço a soma do parametros das duplicidades

    2.2 associo a duplicidade a um dct de duplicidade (que tal lista?)
    2.3 retorno o dct duplicidade
    2.4 este é percorrido e suas linhas são postas em um novo df

    3. SE NÂO tiver duplicidade faço as somas
    3.1 associo as somas a um dct com o parametro como chave
    ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    """
    #aqui cabe a nós criarmos o dicionário que armazena as datas, e se necessário o dicionário que armazena os repetidos
    #esse dicionário de datas com o dicionário de repetidos será armazenado no dctareas2 que será convertido em df
    framebolha2 = pd.DataFrame(dctareas[qual_area][dctareas[qual_area]['Last Applied'] == datasunicas[qual_data]]) #1.
    #Passo das linhas: 7
    dcttemporario = {}
    if framebolha2.shape[0] > 7: #2
        contadorfiltro = 1
        contadorsete = 1
        dctmesmadata = {}

        #VAMO VAMO VAMO!!!
        while contadorfiltro <= int(framebolha2.shape[0]/7):#vou executar esse codigo 2 vezes, eu não preciso executar 7 vezes, vou pulando de 7 em 7, dataframe né
            dctmesmadata[contadorfiltro] = pd.DataFrame(framebolha2.loc[framebolha2.index[(contadorsete * 7) -7]:framebolha2.index[(contadorsete * 7)-1]])
            contadorsete += 1
            contadorfiltro += 1

        contadorfiltro = 1
        #aqui a gente percorre o dct de repetidos e faz as somas, associa os val no outro dct e descarta o dct anterior
        while contadorfiltro <= (framebolha2.shape[0]/7): #2.1
            rate2 = (dctmesmadata[contadorfiltro]['Rate'].replace('---', 0)).sum()
            targetrate2 = (dctmesmadata[contadorfiltro]['Target Rate'].replace('---', 0)).sum()
            totalapplied2 = (dctmesmadata[contadorfiltro]['Total Applied'].replace('---', 0)).sum()
            targettotal2 = (dctmesmadata[contadorfiltro]['Target Total'].replace('---', 0)).sum()
            speed2 = (dctmesmadata[contadorfiltro]['Speed'].replace('---', 0)).sum()
            area2 = (dctmesmadata[contadorfiltro]['Area Applied'].replace('---', 0)).mean()
            data2 = datasunicas[qual_data]
            
            #O uso de variáviel ao invés de uma associação direta ao dct possibilita correções de erros, como em "Target Total", tem valores que são "---"

            field2 = dctareas[qual_area]['Fields'].unique()

            mindct = {}
            mindct['Rate'] = rate2
            mindct['Target Rate'] = targetrate2
            mindct['Total Applied'] = totalapplied2
            mindct['Target Total'] = targettotal2
            mindct['Speed'] = speed2
            mindct['Area Applied'] = area2
            mindct['Last Applied'] = data2
            mindct['Fields'] = field2[0]
        #eu tenho um dct com os parametros (colunas), ou seja uma linha, preciso clocar ela em algum lugar como um df
        #esse while pode retornar tanto um dct de colunas(uma linha) quanto um df ou serie
            dcttemporario[contadorfiltro] = mindct
            contadorfiltro += 1


    else:#3
        rate = (framebolha2['Rate'].replace('---',0)).sum()
        targetrate = (framebolha2['Target Rate'].replace('---', 0)).sum()
        totalapplied = (framebolha2['Total Applied'].replace('---', 0)).sum()
        targettotal = (framebolha2['Target Total'].replace('---', 0)).sum()
        speed = (framebolha2['Speed'].replace('---', 0)).mean()
        area = (framebolha2['Area Applied'].replace('---', 0)).mean()
        data = datasunicas[qual_data]
        #field = dctareas[qual_area]['Fields'][37]

        field = dctareas[qual_area]['Fields'].unique()

        dcttemporario = {}
        dcttemporario['Rate'] = rate
        dcttemporario['Target Rate'] = targetrate
        dcttemporario['Total Applied'] = totalapplied
        dcttemporario['Target Total'] = targettotal
        dcttemporario['Speed'] = speed
        dcttemporario['Area Applied'] = area
        dcttemporario['Last Applied'] = data
        dcttemporario['Fields'] = field[0]

    return dcttemporario

"""
Soma e associa,Como a funcao vai trabalhar?
    Como eu preciso que ela trabalhe?
    O dct areas guarda a referencia para cada area
    Preciso de um novo dct areas que guarde a referencia de cada area com a referencia de datas dentro, e ali sim o df

    Preciso somar as datas iguais e guarda-las em um dataframe da area: beleza
    Preciso somar os valores de 7 em 7 vezes caso o df seja > 7
    
1. Guardar as datas como referencia em um local e usa-las dps

2. Guardar os dataframes das datas

Para isso funcionar primeiro temos um dicionario com os campos guardando um dataframe com as datas
Em seguida podemos armazenar cada data unica em um dicionario
Em seguida armazenamos esse dicionario em um dicionario de campos

>>> dct = {}
>>> dct['area'] = 7
>>> dct2 = {}
>>> dct2['data1'] = 6
>>> dct['area'] = dct2['data1']
>>> dct
{'area': 6}
>>> dct['area'] = dct2
>>> dct
{'area': {'data1': 6}}

    'Rate', 'Total Applied',
       'Target Rate', 'Target Total'

"""


#print(pd.DataFrame(filtradatas(2, 122)))


"""
O que falta?

Já temos uma função que percorre um dct por informação de area e data e nos retorna linhas com as somas

Então preciso associar essas linhas a um dataframe novo conforme percorro o dct

Eu tenho x datas e y areas
preciso percorrer cada uma das datas por cada uma das areas


Proximos passos:
1. Arrumaro o dct dentro do dct
2. Filtrar quais areas possuem um conjunto de dados válido

"""

contadorgeral = 1

dctfinal = {}

contador_areas = 0
contador_datas = 0

"""
O problema do dicionario se resolve aqui
"""

while contador_areas < len(dctareas):

    while contador_datas < datasunicas.shape[0]:

        #print(filtradatas(contador_areas, contador_datas))
        if (pd.DataFrame(dctareas[contador_areas][dctareas[contador_areas]['Last Applied'] == datasunicas[contador_datas]]).empty):
            contador_datas += 1
        else:
            #print(filtradatas(contador_areas, contador_datas) , '\n')
            dctfinal[contadorgeral] = filtradatas(contador_areas, contador_datas)
        #print(dctareas[contador_areas][dctareas[contador_areas]['Last Applied'] == datasunicas[contador_datas]])
       # print(datasunicas[contador_datas])
        
            contadorgeral += 1
            contador_datas += 1

    contador_datas = 0
    contador_areas += 1

#%%
frame3 = pd.DataFrame(dctfinal).T
frame3['Last Applied'] = pd.to_datetime(frame3['Last Applied'])
frame3['Desvio taxa'] = frame3['Rate'] - frame3['Target Rate']
frame3['Desvio litros'] = frame3['Total Applied'] - frame3['Target Total']

frame3.sort_values(by = 'Last Applied')

frame3.drop(frame3[frame3['Rate']< 20].index, inplace=True)
frame3.drop(frame3[frame3['Area Applied']< 5].index, inplace=True)
#frame3.drop(frame3[frame3['Desvio taxa'] < 20].index, inplace=True)

frameestranho = pd.DataFrame(frame3[frame3['Rate'] > 145])


def pede_dados(): #pede_dados(area, data, taxa, )
    #Como voce deseja separar as informações?
    for i in areasunicas:
        print(i)
    for i in datasunicas:
        print(i)
#frame3.to_excel(r'C:/Users/Josué/OneDrive/Dados Agua Clara 1/2022/Estatisticas aplicações/saida1.xlsx')
def plotaoutliers():
    for i in areasunicas:
        
        if frame3[frame3['Fields'] == i].empty:
            pass
        else:
            frameestranho[frameestranho['Fields'] == i].plot(y = ['Target Rate','Rate'], x = 'Last Applied', title = i + '\n Taxas')
            #plt.savefig(f'C:/Users/Josué/OneDrive/Dados Agua Clara 1/2022/Estatisticas aplicações/{i} Grafico Taxas',facecolor = 'w', transparent = False)

            frameestranho[frameestranho['Fields'] == i].plot(x = 'Last Applied', y = 'Area Applied', title = i + '\n Area Aplicada' )
            #plt.savefig(f'C:/Users/Josué/OneDrive/Dados Agua Clara 1/2022/Estatisticas aplicações/{i} Grafico Area aplicada',facecolor = 'w', transparent = False)
            
            frameestranho[frameestranho['Fields'] == i].plot(x = 'Last Applied', y = ['Total Applied', 'Target Total'], title = i + '\n Consumo total' )
            #plt.savefig(f'C:/Users/Josué/OneDrive/Dados Agua Clara 1/2022/Estatisticas aplicações/{i} Grafico Consumo total',facecolor = 'w', transparent = False)
            
            frameestranho[frameestranho['Fields'] == i].plot(x = 'Last Applied', y = 'Speed', title = i + '\n Velocidade Média' )
            #plt.savefig(f'C:/Users/Josué/OneDrive/Dados Agua Clara 1/2022/Estatisticas aplicações/{i} Grafico Velocidade Média',facecolor = 'w', transparent = False)

def plotatudo():
    for i in areasunicas:
        print(i)
        if (frame3[frame3['Fields'] == i].empty == False):
            
            frame3[frame3['Fields'] == i].plot(y = ['Target Rate','Rate'], x = 'Last Applied', title = i + '\n Taxas')
            #plt.savefig(f'C:/Users/Josué/OneDrive/Dados Agua Clara 1/2022/Estatisticas aplicações/{i} Grafico Taxas',facecolor = 'w', transparent = False)

            frame3[frame3['Fields'] == i].plot(x = 'Last Applied', y = 'Area Applied', title = i + '\n Area Aplicada' )
            #plt.savefig(f'C:/Users/Josué/OneDrive/Dados Agua Clara 1/2022/Estatisticas aplicações/{i} Grafico Area aplicada',facecolor = 'w', transparent = False)
            
            frame3[frame3['Fields'] == i].plot(x = 'Last Applied', y = ['Total Applied', 'Target Total'], title = i + '\n Consumo total' )
            #plt.savefig(f'C:/Users/Josué/OneDrive/Dados Agua Clara 1/2022/Estatisticas aplicações/{i} Grafico Consumo total',facecolor = 'w', transparent = False)
            
            frame3[frame3['Fields'] == i].plot(x = 'Last Applied', y = 'Speed', title = i + '\n Velocidade Média' )
            #plt.savefig(f'C:/Users/Josué/OneDrive/Dados Agua Clara 1/2022/Estatisticas aplicações/{i} Grafico Velocidade Média',facecolor = 'w', transparent = False)
            frame3[frame3['Fields'] == i].plot(x = 'Last Applied', y = 'Desvio taxa', title = i + '\n Desvios de taxas' )
            frame3[frame3['Fields'] == i].plot(x = 'Last Applied', y = 'Desvio litros', title = i + '\n Desvios de litros' )
#frame3.plot(x = 'Last Applied', y = ['Rate', 'Target Rate'])

bolha_taxa = frame3[frame3['Fields'] == 'Pivo 3']
bolha_taxa = bolha_taxa[bolha_taxa['Area Applied'] > 40 ]['Last Applied']
print(frame3[frame3['Last Applied'] == '2022-07-22'])
#frame3[frame3['Fields'] == 'Pivo 3'].plot(x = 'Last Applied', y = 'Area Applied', title =  '\n Area Aplicada' )


# %%
print(areasunicas)

# %%

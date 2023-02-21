# -*- coding: utf-8 -*-
"""
Criado dia 22/12/2022 10:00

1. Analisar os dados e ver como estão

Como ocorreu o lançamento dos dados, que fatores na hora de lançar afetam os dados?
Quais as colunas?
Como saber quais dados eu quero separar?
Quais os minimos e mácimos?
O que não vou usar (drop)

Os dados que alimentam essa tabela vem por meio das folhas, existe como saber o volume total por área?
Os dados presentes nessa tabela não possuem a quantia de água gasta, apenas de produto. Uma opção é cruzá-los com os dados do pv.

2. Onde quero chegar?
Quero poder ver os dados por perídos de tempo que eu pedir
Encima disso poder fazer operações entre outras variáveis para determinar valores.

Separar por perído de tempo e área
1. todas as áreas que foram aplicadas de datas x a datas y
1.1 dessas datas e áreas todas que foram uma determinada taxa
1.2 dessas datas e áreas todas que fugiram um valor > x de volume, e quais

2. todas as aplicações em uma área x
2.1 Aplicações de um intervalo de datas na area x
2.2 Aplicações de uma taxa específica na area x
2.3 Aplicações de uma taxa específica na area x em um intervalo de datas
2.4 Variação de litragem com o passar do tempo na area x em um intervalo definido
2.5 Variação total de litragem por área em intervalos de tempo, 
2.6 Variação média por aplicações, por tamanho de área aplicada 

Incógnita:
Utilização de determinados produtos em decorrer do tempo
Para isso o usuário precisa saber primeiro as opções, intervalo de tempo disponível, cultura onde foi aplicado, produtos aplicados
Ex: cultura: soja, aplicações na soja
    Cultura: milho...



Ainda existe a possibilidade se separar por produto.

Tente não complicar.

"""
#%%

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Definições básicas, onde estão os nomed de colunas e onde se encontram os dados que quero
frame_aegro = pd.DataFrame(pd.read_excel('AtividadesSafraSoja2223_21-12-22_16_37_23_Aegro.xlsx', index_col=None))
frame_aegro.columns = frame_aegro.loc[7]
frame_aegro.drop(frame_aegro.loc[0:7].index, inplace=True)
frame_aegro.drop(frame_aegro[frame_aegro['Operação'] != 'Defensivo'].index, inplace=True)

#pd.set_option('display.max_columns', None)

"""
Linha com os nomes de colunas: 7
Início dos dados: 8

nan
Nome área
Área total
nan
Código
Operação
Área da operação
nan
nan
Data inicial
nan
Data final
Tipo
Nome
Classe Toxicológica
Intervalo de segurança
Quantidade
nan
Dose
nan
Equipe
Observações

0    2022-10-10
1    2022-10-25
2    2022-10-26
3    2022-10-27
4    2022-11-03
5    2022-11-04
6    2022-11-05
7    2022-11-07
8    2022-11-09
9    2022-11-11
10   2022-11-16
11   2022-11-17
12   2022-11-21
13   2022-11-18
14   2022-11-23
15   2022-11-25
16   2022-11-26
17   2022-12-02
18   2022-11-30
19   2022-11-28
20   2022-11-29
21   2022-02-12
22   2022-11-24
23   2022-11-08
24   2022-12-03
25   2022-12-01
26   2022-12-09
27   2022-12-10
28   2022-12-15
29   2022-12-05
30   2022-12-12
31   2022-12-16
32   2022-12-07
33   2022-12-20
34   2022-12-19

"""

#Valores individuais de cada coluna
areas = pd.Series(frame_aegro['Nome área'].unique())
codigos = pd.Series(frame_aegro['Código'].unique())
datas_inicio = pd.Series(pd.to_datetime(frame_aegro['Data inicial'].unique()))
datas_fim = pd.Series(frame_aegro['Data final'].unique())
tamanho_areas = pd.Series(frame_aegro['Área total'].unique())

def exibe():
    print(datas_inicio.min())
    print(datas_inicio.max())
    print('tam datas',datas_inicio.shape[0], datas_fim.shape[0])
    print('nomes', areas.shape[0])
    print('tamanho tot', frame_aegro.shape[0])
    
"""
Objetivo: fazer um df com todos os valores somados
Como essas entidades se comportam?




"""
def associa_dct():
    #associacao de cada codigo de ap a um df, e colocando sua referencia em um dct
    #Esse passo é importante para a soma e criação de uma tabela única (ele é?)
    cont_codigo = 0
    cont_area = 0
    cont_data = 0
    while cont_codigo < codigos.shape[0]:
        dctcodigos[codigos[cont_codigo]] = pd.DataFrame(frame_aegro[frame_aegro['Código'] == codigos[cont_codigo]])
        cont_codigo += 1

    while cont_area < areas.shape[0]:
        dctareas[areas[cont_area]] = pd.DataFrame(frame_aegro[frame_aegro['Nome área'] == areas[cont_area]])
        cont_area += 1

    while cont_data < datas_inicio.shape[0]:
        dctdatas[datas_inicio[cont_data]] = pd.DataFrame(frame_aegro[frame_aegro['Data inicial'] == datas_inicio[cont_data]])
        cont_data += 1

"""
O que desejo fazer?
Desejo percorrer cada area por cada data, não o contrário.
Armazenar os valores encontrados, e parar somente quando concluir a lista.



MAPA
associa_dct()
    dctareas[]
    dctdatas[]
    dctcodigos[]

    A POSIÇÃO PERCORRIDA DO DCT DEVE SER ARMAZENADA, A POSIÇÃO DA LISTA DE AREAS NÃO.
    valido para o dct mais interno, 

soma_param()
    enquanto x < len(dctareas)
        percorrer o dctareas
        frame = pd.dataframe(dctareas[areas[x]])
        enquanto y < len(dctdatas)
            percorrer dctdatas
            frame = pd.dataframe

"""

def soma_param():
    conta_areas = 1
    while conta_areas < len(dctareas):
        framesoma = pd.DataFrame(dctareas[areas[conta_areas]])
        conta_datas = 1
        while conta_datas < len(dctdatas):
            if ((framesoma[framesoma['Data inicial'] == datas_inicio[conta_datas]]).empty) == False:
                print(framesoma[framesoma['Data inicial'] == datas_inicio[conta_datas]])
                datas_serie = pd.Series([],[])
                datas_serie['Nome área'] = areas[conta_areas]
                datas_serie['Área total'] = framesoma['Área total'].mean()
                datas_serie['Código'] = framesoma['Código'].mean()
                datas_serie['Operação'] = framesoma.loc[1]['Operação']
                datas_serie['Área da operação'] = framesoma['Área da operação'].mean()
                datas_serie['Data inicial'] = datas_inicio[conta_datas]
                datas_serie['Área da operação'] = framesoma['Área da operação'].mean()
                datas_serie['Quantidade'] = framesoma['Quantidade'].sum()

            conta_datas += 1
        

        conta_areas += 1





"""
---------------------------------------------------------------------------------------------
Execução
---------------------------------------------------------------------------------------------
"""
dctcodigos = {}
dctareas = {}
dctdatas = {}
associa_dct() #essa função depende da existência desses dicionários
frameeee = pd.DataFrame(dctareas[areas[3]])
print(frameeee[frameeee['Data inicial'] == datas_inicio[16]])
soma_param()

# %%

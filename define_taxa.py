import pandas as pd

#tabela2022 = pd.read_excel(r'C:\Users\Josué\OneDrive\Dados Agua Clara 1\Analises de solo Agua Clara Final Análises python.xlsx', sheet_name="2021-2022", index_col=0)
#tabela2021 = pd.read_excel(r'C:\Users\Josué\OneDrive\Dados Agua Clara 1\Analises de solo Agua Clara Final Análises python.xlsx', sheet_name="2020-2021", index_col=0)

with pd.ExcelFile(r'C:\Users\Josué\OneDrive\Dados Agua Clara 1\Analises de solo Agua Clara Final Análises python.xlsx') as xlsx:
    tabela2022 = pd.read_excel(xlsx, "2021-2022")
    tabela2021 = pd.read_excel(xlsx, "2020-2021")

newdata = pd.concat([tabela2022, tabela2021])
print(newdata)

print(newdata.shape)


a = newdata.columns



print(a)



with open(r'C:\Users\Josué\OneDrive\Dados Agua Clara 1\analise1.txt', 'w') as doc1:
    doc1.write(f'{str(analise1)} \n {str(sorted_c)}')


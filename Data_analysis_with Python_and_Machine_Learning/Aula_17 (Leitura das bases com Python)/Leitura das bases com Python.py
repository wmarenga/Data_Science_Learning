import pandas as pd
import csv
import os

" Ler do Excel "
dfClientes = pd.read_excel('caso_estudo.xlsx', sheet_name = 'clientes')
dfLojas = pd.read_excel('caso_estudo.xlsx', sheet_name = 'lojas')
dfProdutos = pd.read_excel('caso_estudo.xlsx', sheet_name = 'produtos')
dfVendas = pd.read_excel('caso_estudo.xlsx', sheet_name = 'vendas')
dfPagamentos = pd.read_excel('caso_estudo.xlsx', sheet_name = 'pagamentos')
print(dfClientes)
print(dfLojas)
print(dfProdutos)
print(dfVendas)
print(dfPagamentos)


" Ler do CSV "
path_csv_clientes ='D:/23) Programação/Cursos/Python/5) Analise de dados com Python e Machine Leearning/Aula_17 (Leitura das bases com Python)/caso_estudo_clientes.csv'
path_csv_lojas ='D:/23) Programação/Cursos/Python/5) Analise de dados com Python e Machine Leearning/Aula_17 (Leitura das bases com Python)/caso_estudo_lojas.csv'
path_csv_produtos ='D:/23) Programação/Cursos/Python/5) Analise de dados com Python e Machine Leearning/Aula_17 (Leitura das bases com Python)/caso_estudo_produtos.csv'
path_csv_vendas ='D:/23) Programação/Cursos/Python/5) Analise de dados com Python e Machine Leearning/Aula_17 (Leitura das bases com Python)/caso_estudo_vendas.csv'
path_csv_pagamentos ='D:/23) Programação/Cursos/Python/5) Analise de dados com Python e Machine Leearning/Aula_17 (Leitura das bases com Python)/caso_estudo_pagamentos.csv'

" Precisamos acrescentar o paramentro (sep = ;), pois o separador padrao do csv e um separador com virgula (,)"
dfClientes2 = pd.read_csv(path_csv_clientes, sep = ';')
dfLojas2 = pd.read_csv(path_csv_lojas, sep = ';')
dfProdutos2 = pd.read_csv(path_csv_produtos, sep = ';')
dfVendas2 = pd.read_csv(path_csv_vendas, sep = ';')
dfPagamentos2 = pd.read_csv(path_csv_pagamentos, sep = ';')
print(dfClientes2)
print(dfLojas2)
print(dfProdutos2)
print(dfVendas2)
print(dfPagamentos2)

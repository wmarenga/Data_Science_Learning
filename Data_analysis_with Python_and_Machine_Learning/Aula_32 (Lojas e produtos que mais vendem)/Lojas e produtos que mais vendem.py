import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

dfclientes = pd.read_excel('caso_estudo.xlsx', sheet_name='clientes')
dflojas = pd.read_excel('caso_estudo.xlsx', sheet_name='lojas')
dfprodutos = pd.read_excel('caso_estudo.xlsx', sheet_name='produtos')
dfvendas = pd.read_excel('caso_estudo.xlsx', sheet_name='vendas')
dfpagamentos = pd.read_excel('caso_estudo.xlsx', sheet_name='pagamentos')

dfclientes.loc[dfclientes.nome.isnull(), 'nome'] = 'Sem Nome'
dfclientes.loc[dfclientes.sexo.isnull(), 'sexo'] = 'O'
dfclientes.loc[dfclientes.dt_nasc.isnull(), 'dt_nasc'] = '1/1/2020'

dfprodutos.loc[9,'valor'] = dfprodutos.valor[9]/10000
dfclientes.dt_nasc = pd.to_datetime(dfclientes.dt_nasc, format= '%m/%d/%Y')

dfclientes = dfclientes.set_index('id')
dflojas = dflojas.set_index('id')
dfprodutos = dfprodutos.set_index('id')
dfvendas = dfvendas.set_index('id')
dfpagamentos = dfpagamentos.set_index('id')

df_juncao = dfvendas.join(dfclientes.add_prefix('clientes_'), on='id_cliente')
df_juncao = df_juncao.join(dflojas.add_prefix('lojas_'), on='id_loja')
df_juncao = df_juncao.join(dfprodutos.add_prefix('produto_'), on='id_produto')
df_juncao = df_juncao.join(dfpagamentos.set_index('id_venda'))

print(df_juncao)
print(df_juncao.isnull().sum())

" ## Feature Engineering ## "

""" Incluindo uma nova coluna de pagamentos (pg) e defimimdo com 1 para dizer que todas as vendas 
tiveram pagamentos """
df_juncao['pg'] = 1
print(df_juncao)

""" Alterando todos os registros sem pagamentos para 'Inadimplente'
df.loc[nome_linha, nome_coluna]"""
df_juncao.loc[df_juncao.dt_pgto.isnull(), 'pg'] = 0
print(df_juncao)

" Criando o dados de tempo de pagamento "
tempo_pgto = df_juncao.dt_pgto - df_juncao.dt_venda
print(tempo_pgto)

" Retirando o (days) do DataFrame, fazendo com que a informacao seja convertida para numeros "
df_juncao['tempo_pg'] = (df_juncao.dt_pgto - df_juncao.dt_venda).dt.days
print(df_juncao)

" Criando a idade dos clientes (O comando 'pd.to_datetime('today')' pega a data atual"
" Usamos estecomando do numpy para converter para anos (/np.timedelta64(1,'Y')"
print((pd.to_datetime('today') - df_juncao.clientes_dt_nasc)/np.timedelta64(1,'Y'))

" Acrescentando no inicio da sequencia de comando o comando (np.floor), teremos um arredondamento para baixo"
print(np.floor((pd.to_datetime('today') - df_juncao.clientes_dt_nasc)/np.timedelta64(1,'Y')))

" Armazenando os dados gerados em uma nova coluna chamada ('cliente_idade')"
df_juncao['cliente_idade'] = np.floor((pd.to_datetime('today') - df_juncao.clientes_dt_nasc)/np.timedelta64(1,'Y'))
print(df_juncao)

" Analise de lojas e produtos que mais vendem "

" Com este comando podemos ajustar quantas colunas serao exibidas"
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 120)

print(df_juncao)

" Contabilizando todos os dados pelas lojas das cidades "
print(df_juncao.groupby('lojas_cidade').count())

" Somando todos os dados pelas lojas das cidades "
print(df_juncao.groupby('lojas_cidade').sum())

" Somando apenas os dados das lojas das cidades para (produto_valor) = receita de cada loja"
print(df_juncao.groupby('lojas_cidade').sum().produto_valor)

" Contagem da quantidade de venda apenas das lojas das cidades para (produto_valor)"
print(df_juncao.groupby('lojas_cidade').count().produto_valor)

" Ordenando a contagem de quantidade de venda apenas das lojas das cidades para (produto_valor)"
print(df_juncao.groupby('lojas_cidade').count().produto_valor.sort_values(ascending=False))

" Inserir o groupby de vendas por cidades em uma variavel "
graf_dados = df_juncao.groupby('lojas_cidade').count().produto_valor.sort_values(ascending=False)
print(graf_dados)

" Criando um grafico no matplotlib (vendas por loja)"
plt.figure(figsize=(15,5))
plt.bar(graf_dados.index, graf_dados.values)
plt.title('Vendas por Loja')
plt.show()

" Avaliando a quantidade de produtos que mais vendem "

" Contabilizando todos os dados dos produtos, considerando produto_valor como a informacao mais relevante "
print(df_juncao.groupby('produto_produto').count().produto_valor)

" Ordenando a contagem de quantidade de produtos, considerando produto_valor como a informacao mais relevante)"
print(df_juncao.groupby('produto_produto').count().produto_valor.sort_values(ascending=False))

" Armazenado o groupby de produtos em uma variavel "
graf_dados = df_juncao.groupby('produto_produto').count().produto_valor.sort_values(ascending=False)
print(graf_dados)
print(graf_dados.index)
print(graf_dados.values)

" Criando um grafico no matplotlib (Vendas por Produtos)"

plt.figure(figsize=(15,5))
plt.bar(graf_dados.index, graf_dados.values)
plt.title('Vendas por Produto')
plt.show()
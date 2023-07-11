import pandas as pd
import matplotlib.pyplot as plt

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

" Analise Preliminar "

" Exibe uma amostra aleatoria dos dados do DataFrame "
print(dfClientes.sample(5))

" Exibe os 5 primeiros dados do DataFrame "
print(dfClientes.head(5))

" Exibe os 5 ultimos dados do DataFrame "
print(dfClientes.tail(5))

" Descobrindo quais sao os dados nulos "
print(dfClientes.isnull())

" Descobrindo quantos sao os dados nulos "
print(dfClientes.isnull().sum())

" Identificando especificamente quais sao os registros nulos "
" Primeiro transpor a tabela )invertemos linhas com colunas "
print(dfClientes.isnull().T)

" Verificamos se cada linha da tabela possui registro nulo ou nao "
print(dfClientes.isnull().T.any())

" Para saber quais sao exatamente, usamos o comando acima como filtro do DataFrame "
print(dfClientes[dfClientes.isnull().T.any()])

" Avaliando a coluna 'sexo' para buscar os valores unicos "
print(dfClientes.sexo.unique())
" Verificamos que existe 'M', 'F' e 'nan'. Deixar o 'nan' podera causar problema no tratamento dos dados "
" Deletar simplesmente o registro pode nao ser adequado, pois estariamos eliminado um dados relevante para no analise futura "

" Avaliando o dfLojas "
print(dfLojas)
" Todos os registro parecem estar consistentes "

" Avaliando o dfLojas "
print(dfProdutos)
" Verificamos um nome estranho xxx-231a"

" Verificamos que todos os valores foram identificados como numeros "
print(dfProdutos.describe())

" Identificando graficamente "

dfProdutos.boxplot(column=['valor'])
plt.show()
" As bolas mostram valores fora do conjunto de dados"

" Identificando os valores que estao fora do conjunto de dados"
print(dfProdutos[dfProdutos.valor > 3000000])

" Gerando um grafico, onde retiramos este valor discrepante "
" definindo um filtro para o DataFrame "
dfProdutos[dfProdutos.valor<3000000].boxplot(column=['valor'])
plt.show()

" Verificando se o produto discrepante (xxx-231a) foi realmente vendido "
print(dfVendas[dfVendas.id_produto ==10])

"Verificamos que temos 182 vendas para este produto, sendo assim este produto nao pode ser excluido "
print(dfVendas[dfVendas.id_produto ==10].count())

" Verificando se existe algum valor nulo no dfVendas "
print(dfVendas.isnull().sum())
" Nao existe nenhum valor nulo "

" Verificamos se os dados do DataFrame fazem sentido "
print(dfVendas.describe())
""" 
- id_clinte possui min = 1 e max=1000 (correto pois temos 1000 clientes)
- id_loja possui min = 1 e max = 10 (correto pois temos 10 lojas)
- id_produto possui min = 1 e max = 10 (correto pois temos 10 produtos)
"""

" Avaliando o DataFrame pagamentos "
" Verificar se existe algum dado nulo "
print(dfPagamentos.isnull().sum())

print(dfPagamentos.describe())
" id_vendas max = 2997 (correto pois e menor do que id_vendas que e 3000)"
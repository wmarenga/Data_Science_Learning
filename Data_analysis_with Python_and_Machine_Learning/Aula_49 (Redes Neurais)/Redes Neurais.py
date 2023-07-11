""" 
Machine Learning:

Precisamos usar tecnicas de Machine Learning para responder a pergunta abaixo. 
- E possivel prever inadimplencia atraves dos dados idade, cidade e produto?

Conceito de Machine Learning:

- Definicao de um alvo (uma coluna os linha do DF);
- Normalizar dados (os dados devem estar na mesma grandeza);
- Dados categoricos, nao representam uma sequencia (Ex. nome de cidade);
- Dados de treinamento (separamos entre 70% a 80% para treinamento do algoritmo), este treinamento e necessario para que o 
algoritmo aprenda sobre a informacao e de teste (o restante da informacao, 20% a 30% e utilizado para teste). Se o algoritmo 
performe muito bem no treinamento e muito mal no teste, ocorreu um 'Overfit'. O algoritmo decorou os dados do treinamento, porem
nao consegue ir bem no teste;
- Escolher um modelo;
- Matriz de confusao : E usada para avaliar o resultado do modelo.
 Temos nas linhas o valor real e nas colunas o valor predito. 
 Os Verdadeiros Postivo (TP) e Verdadeiros Negativo (TN) sao acertos do algoritmo. 
 Os Falsos Postivo (FP) e Falsos Negativo (FN) sao erros no algoritmo. 
 
                    Valor Predito
                |      SIM       |       NAO
--------|-------|----------------|----------------
        | SIM   |   Verdadeiro   |     Falso 
Real    |       |  Positivo (TP) |  Negativo (FN)
--------|-------|----------------|----------------
        | NAO   |  Falso         |  Verdadeiro
        |       | Positivo (FP)  |  Negativo (TN)

Com isto, craimos metricas muito importantes em Machine Learning, que sao a PRECISAO e o RECALL. 

Precisao: Informa o quanto o algoritmo acertou dos valores preditos (90% - cada 10 previsoes, 9 estao corretas). 

Recall: Ele mostra dos dados que aconteceram, o quanto o algoritmo capturou (Ex. tivemos 10 dados historicos decorrentes de um evento,
e o algoritmo capturou 9, sendo assim o Recall de 90%). (Recall == Captura)

Precisao e Racall sao antagonico, pois um presa pela precisao e o outro pela captura. 

                    Precisao
                |  0  |   1
--------|-------|-----|-------
Recall  |   0   |  VP |   FN    <------
        |-------|-----|--------
        |   1   |  FP |   VN
--------|-------|-----|--------
                   /\
                    |

Precisamos primeiramente criar o modelo:

O comando normalmente e (model = modelo(parametros))
As palavras (modelo e parametros) serao alteradas de acordo com o modelo que desejamos usar. 
Apos isso nos usamos o comando (model.fit(X, y))
X - sao as colunas Dado 1, Dado 2 e Dado 3
y - e a coluna (Target)

Feito esta etapa o modelo ja esta treinado e criado. 

Dado 1  | Dado 2  |  Dado 3  |  Target
   A    |    D    |     G    |    0
   B    |    E    |     H    |    1
   C    |    F    |     I    |    1

Agora temos que utilizar o algoritmo. 
Para usar-lo podemos utilizar o comando (model.predict(X) ==> Target = 1)

Dado 1  | Dado 2  |  Dado 3  |  Target
   A    |    E    |     I    |   ???

"""
from logging import PercentStyle
from turtle import left
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter
import numpy as np
import seaborn as sns

caminho_arquivo_Excel_prom ='D:/23) Programação/Cursos/Python/5) Analise de dados com Python e Machine Leearning - 5 horas/Aula_49 (Redes Neurais)/caso_estudo_venda_promocao.csv'
dfclientes = pd.read_excel('caso_estudo.xlsx', sheet_name='clientes')
dflojas = pd.read_excel('caso_estudo.xlsx', sheet_name='lojas')
dfprodutos = pd.read_excel('caso_estudo.xlsx', sheet_name='produtos')
dfvendas = pd.read_excel('caso_estudo.xlsx', sheet_name='vendas')
dfpagamentos = pd.read_excel('caso_estudo.xlsx', sheet_name='pagamentos')
dfPromo = pd.read_csv(caminho_arquivo_Excel_prom, sep=";")

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
dfPromo = dfPromo.set_index('id_venda')

df_juncao = dfvendas.join(dfclientes.add_prefix('clientes_'), on='id_cliente')
df_juncao = df_juncao.join(dflojas.add_prefix('lojas_'), on='id_loja')
df_juncao = df_juncao.join(dfprodutos.add_prefix('produto_'), on='id_produto')
df_juncao = df_juncao.join(dfpagamentos.set_index('id_venda'))
df_juncao = df_juncao.join(dfPromo)

df_juncao['pg'] = 1
df_juncao.loc[df_juncao.dt_pgto.isnull(), 'pg'] = 0

tempo_pgto = df_juncao.dt_pgto - df_juncao.dt_venda
df_juncao['tempo_pg'] = (df_juncao.dt_pgto - df_juncao.dt_venda).dt.days

df_juncao['cliente_idade'] = np.floor((pd.to_datetime('today') - df_juncao.clientes_dt_nasc)/np.timedelta64(1,'Y'))

" Com este comando podemos ajustar quantas colunas serao exibidas"
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 120)

#print(df_juncao)

" O objetivo e discutir os dados e a construcao do modelo e nao a programacao em si "

import copy

" Devemos criar um novo df com dados significativos, por este motivo devemos retirar dados redundantes (id_loja e lojas_cidade)"
" Por este motivo, nos criaremos um novo DataFrame chamado (dfML) "
""" Algumas colunas foram omitidas, pois nao trazem informacoes para trabalharmos com previsoes. Informacoes como nome do cliente,
data de nasc (ja temos clientes_idade), data_venda, dt_pagto, etc, nao seriam relevantes na nossa analise"""
dfML = df_juncao[['clientes_sexo', 'lojas_cidade', 'produto_produto', 'produto_valor', 'cliente_idade', 'promoção', 'pg']]
dfML = dfML.replace(['','-'],'_', regex=True)
" Mostramos apenas as colunas de interesse "
#print(dfML)

" Normalizando os dados "
" Existem varias formas de normalizar os dados, tais como: dividir pelo maior valor (inf variando de 0 a 1) "
" O conceito de normalizacao e a variacao dos dados entre: -1 e 1 "
" Uma idade e/ou um produto_valor negativos nao fariam sentido, sendo assim iremos utilizar uma variacao entre 0 e 1 "

" Colunas com dados numericos, recebem o valor de mesma dividido pelo seu valor maximo "
dfML['produto_valor'] = dfML['produto_valor']/ dfML['produto_valor'].max()
dfML['cliente_idade'] = dfML['cliente_idade']/ dfML['cliente_idade'].max()
#print(dfML)

" Trabalhando com dados categoricos ('clientes_sexo', 'lojas_cidade', 'produto_produto', 'promoção') "
col_cat = ['clientes_sexo', 'lojas_cidade', 'produto_produto', 'promoção']
" O pandas tem uma funcao excelente para separar as colunas em subcolunas de dados categoricos "
" A funcao apos separar as colunas, acrescentou o numero 1 para cada linha com a informacao presente e zero para ausente "
dfML_dummies = pd.get_dummies(dfML[col_cat].astype(str), drop_first=False)
#print(dfML_dummies)

" Agora iremos juntar os dados do dfML_dummies com o dfML "
dfML = pd.concat([dfML, dfML_dummies], axis=1)
" O comando .drop exclui as colunas anteriores ('clientes_sexo', 'lojas_cidade', 'produto_produto', 'promoção') "
dfML = dfML.drop(col_cat, axis=1)
print(dfML)

" A partir deste momento o dfML possui apenas informacoes numericas "

" Agora iremos utilizar a biblioteca (sklearn), esta biblioteca e excelente para Machine Learning "

from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_auc_score, roc_curve, classification_report,accuracy_score
from sklearn.metrics import recall_score, precision_score, f1_score, confusion_matrix, auc

" O y e o Target (dados de saida) "
y = dfML.pg
" E o DataFrame ML exceto a coluna (pg) - (dados de entrada)"
X = dfML.drop(['pg'], axis=1)
" Este comando ira separar aleatoriamente os dados entre treinamento e teste em uma proporcao de 70% e 30%"
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

" Com este comando estamos simulando uma nova venda "
" Cada um possui um pg == 1 [2997] e um pg == 0 [2998]"
X_new = X.loc[[2997,2998]]
print(X_new)

" ## REGRESSAO LINEAR E REGRESSAO LOGISTICA ## "

""" A Regressao linear (dados continuos) e aplicada quando baseado em um eixo numerico eu quero prever um outro eixo numerico. Os dados sao
distribuidos no grafico de forma que eu posso gerar uma reta para prever valores nesta reta baseado no eixo que quero prever. 

A Regrecao Logistica (dados binarios) em que a minha saida deveria ser zero (0) ou um (1). 

"""

" Regressao Logistica "
import statsmodels.api as sm
import statsmodels.formula.api as smf
from sklearn.linear_model import LogisticRegression

#all_col_with_plus = ' + '.join(dfML.drop(['pg'], axis=1).columns)
#modelo = smf.glm(formula='pg ~ ' + all_col_with_plus, data=dfML, family = sm.families.Binomial()).fit()
#print(modelo.summary())

model = LogisticRegression(penalty='none', solver='newton-cg')
model.fit(X_train, y_train)

print('- Matriz de Confusão')
print(confusion_matrix(y_test, model.predict(X_test)))
print('\n- Reporte completo')
print(classification_report(y, model.predict(X)))
print('\n- Reporte teste')
print(classification_report(y_test, model.predict(X_test)))

print(model.predict(X_new))
" Previu que a primeira compra ira gerar pagamento e a segunda nao "

" ## ARVORE DE DECISAO ## "
" A arvore de decisao fornece maior controle sobre os ramos de decisao da arvore "
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn import metrics, tree

model = DecisionTreeClassifier(criterion="entropy", max_depth=5)
model = model.fit(X_train,y_train)
fig = plt.figure(figsize=(20,10))
_ = tree.plot_tree(model, feature_names=X.columns, class_names=['targetNo','targetYes'], filled=True)
plt.show()

print('- Matriz de Confusão')
print(confusion_matrix(y_test, model.predict(X_test)))
print('\n- Reporte completo')
print(classification_report(y, model.predict(X)))
print('\n- Reporte teste')
print(classification_report(y_test, model.predict(X_test)))

print(X_new)
print(df_juncao.loc[X_new.index])

print(model.predict(X_new))

" ## REDES NEURAIS ## "

" A biblioteca keras e muito famosa (do Google)"

from keras import Sequential
from keras.layers import Dense
import keras
import tensorflow
tensorflow.random.set_seed(2)

" Dense e a quantidade de neuronios "
model = Sequential()
model.add(Dense(15, activation='relu', kernel_initializer='random_normal', input_dim=len(X.columns)))
model.add(Dense(7, activation='relu', kernel_initializer='random_normal'))
model.add(Dense(3, activation='relu', kernel_initializer='random_normal'))
model.add(Dense(3, activation='relu', kernel_initializer='random_normal'))
model.add(Dense(1, activation='sigmoid', kernel_initializer='random_normal'))

" Compilacao do modelo "
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
" Definicao da execucao do modelo , treinamento do modelo "
model.fit(X_train,y_train, batch_size=128, epochs=300, verbose=False)

print('- Matriz de Confusão')
print(confusion_matrix(y_test, model.predict_classes(X_test)))
print('\n- Reporte completo')
print(classification_report(y, model.predict_classes(X)))
print('\n- Reporte teste')
print(classification_report(y_test, model.predict_classes(X_test)))

print(model.predict(X_new))


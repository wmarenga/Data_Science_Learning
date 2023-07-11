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
" Lacos Condicionais: FOR, WHILE e IF "

" ## LISTAS ## "
" Toda lista e criada entre colchetes [] e podendo ser alterada e/ou inserir dados a qualquer momento "
nomes = ['Rafael', 'Maria', 'Ana']
idades = [10,20,15]

" ## TUPLAS ## "
" Toda Tupla e criada entre aspas () e NAO podendo ser alterada ou inserir informacoes "
sexo = ('M', 'F', 'O')

" ## DICIONARIOS ## "
" Todo dicionario e criado entre parenteses {}, possuindo uma chave antes dos : e depois dos : podemos inserir valor (int, listas, tuplas, str) "
cadastro = {'nomes': nomes, 'idades':idades, 'cidade': ['A', 'B', 'C']}

for nome in nomes:
    print(nome)
    
for idade in idades:
    " Podemos rodar o if e print na mesma linha "
    if idade%2 == 0:    print(idade)

" o ultimo algoritimo nao entra no laco for (10)"
for i in range(0,10):
    print(i)

i = 0
idade = idades[i]
while idade <= 10:
    print(idade)
    i += 1
    idade = idades[i]
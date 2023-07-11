" Fumcoes em Python "

" Chamando a funcao "

import sys, os
" Adicionar um diretorio padrao no pythonpath "
sys.path.insert(0,'d:\\23) Programação\\Cursos\\Python\\5) Analise de dados com Python e Machine Leearning\\Aula_8_Funcoes')

" Linha de comando para chamar um modulo externo "
sys.path.insert(0,os.path.abspath(os.curdir))

import Aula_8_Funcoes.Functions as mf

print(mf.faixaIdade(10))

print(mf.faixaIdade(17))

print(mf.faixaIdade(45))

print(mf.faixaIdade(81))

" Exibir o $pythonpath"
print(sys.path)

print(mf.somaQuad(2,4))
# importando sqlite
import sqlite3 as lite  # o comando 'as' me permite mudar o nome de qualquer coisa dentro do python para ficar menor. Nesse caso estou mudando o nome sqlite3 para lite
# Criando novo banco de dados / criando conexão
conexao = lite.connect('clientes.db')  # criando conexão entre o python e o banco de dados clientes
# Criando tabelas no banco de dados
# Tabela clientes
with conexao:
    cur = conexao.cursor()
    cur.execute("CREATE TABLE Clientes( nome TEXT, idade INTEGER, PRIMARY KEY('nome'))")

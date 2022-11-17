#1- Voce importa a biblioteca sqlite3

import sqlite3

#2- Vamos estabelecer uma conexão com o banco de dados

conexao = sqlite3.connect("dc_universe.db")

#3o. passo: criar um objeto do tipo cursor

cursor = conexao.cursor()

#4- Comando SQL do branco 

sql = "SELECT pessoa_id, nome, nome_civil, tipo FROM pessoas"

#5o. passo: Executar o comando SQL no SQLlite (no cursor)

cursor.execute(sql)

#6o. passo: Exibir a consulta com todos os nomes de herois e viloes do banco de dados

pessoas = cursor.fetchall()
for pessoa in pessoas:
  print(pessoa)

for pessoa in pessoas:
    print(f"Nome: {pessoa[1]}")
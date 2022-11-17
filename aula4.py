#1o. passo:importar a bliblioteca sqlite3
import sqlite3

#2o. passo:estabelecer conecxao com o banco de dados
conexao = sqlite3.connect("dc_universe.db")

#3o. passo: criar um objeto do tipo cursor
cursor = conexao.cursor()

#4o. passo: comando SQL do banco
sql = "SELECT pessoa_id, nome, nome_civil, tipo FROM pessoas"

#5.o passo: executar o comando SQL no SQLite (no cursor)
cursor.execute(sql)

#6.o passo: exibir a consulta com todos os nomes de herois e vilos do banco de dados
pessoas = cursor.fetchall()
for pessoa in pessoas:
  print(pessoa)
  
for pessoa in pessoas:
  print(f"Nome: {pessoa[1]} ({pessoa[3]})")
  
  
  


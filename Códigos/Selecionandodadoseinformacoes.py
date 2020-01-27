# Importando a biblioteca PyMySql
import pymysql

# conexão com o servido do bando de dados
conexao = pymysql.connect(
    host="85.10.205.173",
    user="mfelippe",
    passwd="MFelippe1",
    database = "databank"
)

''''
As instruções a seguir serve para buscar dados dentro da tabela especificada, fectchall garante
que todos os dados contidos na tabela vai ser lidos, apos isso os dados são listados no laço for


para selecionar apenas o nome é só alterar  a instrução  do SELECT, por exemplo se for só o nome seria 

cursor.execute("SELECT nome FROM usuario")
caso deseja  mais de um dado o mesmo deve ser separado com virgula

para buscar um dados é necessario usar WHERE, EXEMPLO
cursor.execute("SELECT * FROM  usuario WHERE nome = 'julia' ")
'''
cursor = conexao.cursor()
cursor.execute("SELECT * FROM usuario")
resultado = cursor.fetchall()

for x in resultado:
    print(x)
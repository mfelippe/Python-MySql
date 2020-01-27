# Importando a biblioteca PyMySql
import pymysql

# Criando a conexão com o servido do bando de dados
conexao = pymysql.connect(
    host="85.10.205.173",
    user="mfelippe",
    passwd="MFelippe1",
    database ="databank"
)

cursor = conexao.cursor()
'''
instrução de criar tabela
cursor.execute("CREAT TABLE user(nome VARCHAR(50), email VARCHAR(50))")
'''
#instrução para mostrar tabelas

cursor.execute("SHOW TABLES")

for v in cursor:
    print(v)

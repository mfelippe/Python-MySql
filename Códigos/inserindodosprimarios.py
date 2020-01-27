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
#Alterando atributos na tabela
cursor.execute("ALTER TABLE user ADD COLUMN id INT AUTO_INCREMENTE PRIMARY KEY")

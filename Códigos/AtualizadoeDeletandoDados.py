# Importando a biblioteca PyMySql
import pymysql

# Criando a conexão com o servido do bando de dados
conexao = pymysql.connect(
    host="85.10.205.173",
    user="mfelippe",
    passwd="MFelippe1",
    database = "databank"
)
cursor = conexao.cursor()

'''
comando e execuções para atualizações e delete

 -------- Mudando todos os dados de um vez só ---------
con_sql = "UPDATE usuario SET nome = 'Leoncio' "
cursor.execute(con_sql)
conexao.commit()

Após a Instrução Anterior todos os Dados nome na tabela usuario seram setados para Leoncio

------------- APAGANDO dados dentro de uma tabela --------------------
con_sql = " DELETE FROM usuario WHERE nome = 'Leoncio' "
cursor.execute(con_sql)
conexao.commit()

----------- EXCLUINDO Uma  TABELA -------------------------
con_sql = " DROP TABLE usuario"
cursor.execute(con_sql)
conexao.commit()
'''
con_sql = " "
cursor.execute(con_sql)
conexao.commit()
print(cursor.rowcount, "tabela modificada e gravada")
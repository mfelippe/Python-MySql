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

#instruções em SQL

com_sql = "INSERT INTO user(nome, email) VALUES(%s,%s)"
valor = ('Lucio', 'lucio@email.com')
cursor.execute(com_sql, valor)

#comando para gravar todas as instruções
 conexao.commit()

 #comando para saber as linhas que fora inseridas
 print(cursor.rowcount,"inserida com sucesso")

 '''
 Algoritmo para inserir mais de uma linha de dado   <--- o modo de inserir os dados tbm mudam
valor = [('marcelo', 'marcelo@email.com'),
        ('tais', 'tais@email.com'),
        ('tiago', tiago@email.com')]
        
cursor.executemany(com_sql, valor)  <----- essa instrução muda
'''
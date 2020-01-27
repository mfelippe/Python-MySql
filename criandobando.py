import pymysql

conexao = pymysql.connect(
    host ='localhost',
    user = 'admin'
    passwd= ''
)
cursor = conexao.cursor()
#função para criar um bando de dados
cursor.execute("CREATER DATABASE users")

'''
#cursor.execute("SHOW DATABASES") # essa função mostra os bancos de dados listados no servidor

for x in cursor:
    print(x)
'''
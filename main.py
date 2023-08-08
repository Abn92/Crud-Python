import mysql.connector

conexao = mysql.connector.connect(
    host= 'localhost',
    user='root',
    password='',
    database='dbmarcos'
)

cursor = conexao.cursor()

# CRUD
nome = "Teclado"
valor= "50"
comando = f'INSERT INTO vendas(produto,valor) VALUES("{nome}",{valor})'
cursor.execute(comando)
conexao.commit() #edita - insert/update
# resultado = cursor.fetchall()

cursor.close()
conexao.close()
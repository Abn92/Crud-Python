import mysql.connector
from flask import Flask, render_template

# conexao = mysql.connector.connect(
#     host= 'localhost',
#     user='root',
#     password='',
#     database='dbmarcos'
# )


# CRUD

# SELECT
# cursor = conexao.cursor()
# queryselect = f'select * from vendas'
# cursor.execute(queryselect)
# resultado = cursor.fetchall()
# print(resultado)
#
# cursor.close()
# conexao.close()

# INSERT
# cursor = conexao.cursor()
# nome = "Mouse"
# valor= "37"
# comando = f'INSERT INTO vendas(produto,valor) VALUES("{nome}",{valor})'
#
# cursor.execute(comando)
# conexao.commit() #edita - insert/update
#
# cursor.close()
# conexao.close()

# UPDATE
# cursor = conexao.cursor()
# nome = "Mouse Gamer"
# valor= "87"
# comando = f'UPDATE VENDAS SET nome = ("{nome}"),valor = {valor})'
#
# cursor.execute(comando)
# conexao.commit() #edita - insert/update
#
# cursor.close()
# conexao.close()

# DELETE
# cursor = conexao.cursor()
# id = "2"
# comando = f'DELETE FROM VENDAS WHERE id = ("{id}")'
#
# cursor.execute(comando)
# conexao.commit() #edita - insert/update/delete
#
# cursor.close()
# conexao.close()



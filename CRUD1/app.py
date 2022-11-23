import mysql.connector
#criar conexão bd
conexao = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password ='151413',
    database ='bd_crud1'
)

cursor = conexao.cursor()

#crud

#como criar o comando
#comando = ''
#cursor.execute(comando)
#conexao.commit() #edita o banco de dados
#resultado = cursor.fetchall() #ler o banco de dados.

#CREATE
#nome_produto = "toddynho"
#valor = 3
#comando =f'INSERT INTO vendas (nome_produto, valor) VALUES ("{nome_produto}", {valor})'
#cursor.execute(comando)
#conexao.commit()

#READ

#comando =f'SELECT * FROM vendas'
#cursor.execute(comando)
#resultado = cursor.fetchall()
#print(resultado)


#UPDATE
#nome_produto = "toddynho"
#valor = 6
#comando =f'UPDATE vendas SET valor = {valor} WHERE nome_produto = "{nome_produto}" '
#cursor.execute(comando)
#conexao.commit() #Não pode esquecer esse item, se não não altera o bd.



#DELETE
nome_produto = "toddynho"
comando = f'DELETE FROM vendas WHERE nome_produto = "{nome_produto}"'
cursor.execute(comando)
conexao.commit()

cursor.close()
conexao.close()

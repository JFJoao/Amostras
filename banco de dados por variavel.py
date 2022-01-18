import sqlite3

resposta = "S"
# while resposta == "S":
#    nome = input("Informe o nome: ")
#    idade = input("Informe a idade: ")
#    email = input("Informe o email: ")
#    resposta = (input("Digite \"S\" para continuar adicionando.")). upper()
#    banco = sqlite3.connect('quarto_banco.db')
#    cursor = banco.cursor()
#    cursor.execute("INSERT INTO pessoas VALUES ('"+nome+"','"+str(idade)+"','"+email+"')")
#    banco.commit()

banco = sqlite3.connect('quarto_banco.db')
cursor = banco.cursor()

# cursor.execute("CREATE TABLE pessoas (nome text, idade integer, email text)")
# cursor.execute("INSERT INTO pessoas VALUES ('"+nome+"','"+str(idade)+"','"+email+"')")
# cursor.execute("DELETE FROM pessoas WHERE nome like 'mess%' ")
# cursor.execute("UPDATE pessoas SET email = 'thais@gmail.com' WHERE email = 'maria123@gmail.com'")

banco.commit()
# banco.close()

# except sqlite3.Error as error:         #procurar erro
#  print("Erro ao excluir:" ,error)

cursor.execute ("SELECT * FROM pessoas")
print(cursor.fetchall())
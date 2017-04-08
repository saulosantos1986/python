# conexao com o banco

import psycopg2

con = psycopg2.connect(
	"host=%s dbname=%s user=%s password=%s" % (
	'localhost', 'projetos', 'postgres', '4linux123'
	)
)

# Criar um menu com loop

flag = True

while flag:

	banner = '''Menu:

1) Logar
2) Cadastrar
3) Lista usuario
4) sair
Selecione a opcao:'''

	option = int(raw_input(banner))


	if option == 1:
		print 'Opcao 1 selecionada'

		usuario = raw_input ("Digite seu usuario: ")

		senha = raw_input ("Digite sua senha: ")

	elif option == 2:

		print 'Opcao 2 selecionada'

	elif option == 3:

		print 'Opcao 3 selecionada'

	elif option == 4:

		print 'Volte Sempre'
		flag = False

	


# raw input para inserir variavel dentro do banco

titulo = raw_input ("Favor inserir o Titulo: ")

conteudo = raw_input ("Favor inserir o conteudo: ")

# efetuando operacao no banco

cur = con.cursor()

cur.execute("INSERT into posts (titulo, conteudo) values ('%s', '%s')" % (titulo,conteudo))

con.commit()

# buscar o conteudo no banco

cur.execute("SELECT * from posts")

for row in cur.fetchall():
	print 'ID: %s \nTitulo: %s\n Conteudo: %s' % (row)
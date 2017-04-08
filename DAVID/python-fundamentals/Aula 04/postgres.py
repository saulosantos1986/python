#modulo para conectar no banco postgres

import psycopg2

con = psycopg2.connect(
	"host=%s dbname=%s user=%s password=%s" % (
	'localhost', 'projetos', 'postgres', '4linux123'
	)
)

cur = con.cursor()

cur.execute("SELECT * FROM posts")

for row in cur.fetchall():
	print 'ID: %s \nTitulo: %s\n Conteudo: %s' % (row) 



#registro = cur.fetchone() - traz o primeiro registro




# -----------------------INSERT NO BANCO-----------------

#cur = con.cursor()
#cur.execute("\
#INSERT INTO posts(conteudo, titulo)\
#VALUES('SAULO','SANTOS')")

#if cur.rowcount:
#	print 'Registro inserido com sucesso'

#con.commit()

except Exception as e:
	print e
	con.rollback()


#modulo para conectar no banco postgres

import psycopg2

con = psycopg2.connect(
	"host=%s dbname=%s user=%s password=%s" % (
	'localhost', 'projetos', 'postgres', '4linux123'
	)
)

cur = con.cursor()
cur.execute("\
INSERT INTO posts(conteudo, titulo)\
VALUES('SAULO','SANTOS')")

con.commit()

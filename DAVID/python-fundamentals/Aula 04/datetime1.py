from datetime import datetime

acesso = datetime(2016, 01, 22, 00, 00, 00)
atual = datetime.now()

if (atual - acesso).total_seconds() > 3600:

	print "Perdeu acesso"

else:

	print "Acesso Liberado"
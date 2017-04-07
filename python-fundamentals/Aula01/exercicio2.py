idade = int(raw_input("Digite sua idade!:"))
carteira = raw_input("Tem Habilitacao??:")
alcoolizado = raw_input("Voce bebeu??:")


if idade >= 18 and carteira == "S" and alcoolizado == "N":
	
	print 'Pode seguir!'

else:

 	print 'Se fodeu!'
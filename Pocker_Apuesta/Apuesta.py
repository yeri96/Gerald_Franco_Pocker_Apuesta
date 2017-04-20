# coding:utf-8
############################################################################
#                        QUE HACE?
# Apuestas
############################################################################


############################################################################
#                        IMPORT
############################################################################
from random import randint


############################################################################
#                        VARIABLES GLOBALES
############################################################################



############################################################################
#                               NIVEL 4
############################################################################



############################################################################
#                               NIVEL 3
############################################################################



############################################################################
#                               NIVEL 2
############################################################################
def leer_apuesta(saldo,salir,apuesta):
	
	if (saldo<10):
		salir_apuesta=True
		salir=True
	else:	
		salir_apuesta=False
		print "Saldo actual:" , saldo
		print "Apuesta mínima 10€"
		print "Salir: -1"
		apuesta=input("Introduca su apuesta: ")
			
	while (salir_apuesta==False):
		if (apuesta==-1):
			salir_apuesta=True
			salir=True
		else:
			if (apuesta>=10 and apuesta<=saldo):
				saldo=saldo-apuesta
				salir_apuesta=True
			else:
				print "Apuesta incorrecta"
				if (apuesta<10):
					print "La apuesta mínima es de 10€"
				if (apuesta>saldo):
					print "No puede apostar más de su saldo"
				print "Salir: -1"
				apuesta=input("Introduca su apuesta: ")
	return saldo,salir,apuesta
	
############################################################################
#                               NIVEL 1
############################################################################


saldo=100
apuesta=0
salir=False
carta_banca=3
palo_banco="C"
carta_jugador=2
palo_jugador="P"


# Leer apuesta
saldo,salir,apuesta=leer_apuesta(saldo,salir,apuesta)




while (salir==False):
	# Sacar dos cartas
	# Banca= 3 Corazones
	# Yo = 10 picas

	# Quien gana + recalcular saldo?
	# Yo

	# Empate
	if (carta_jugador==carta_banca):
		print "En caso de empate gana la banca"
	else:
		# Gana jugador
		if (carta_jugador>carta_banca):
			print "Usted gana"
			saldo=saldo+(apuesta*2)
		else:
			print "LOOSER!!!"
	
	
#	print "Saldo actual:" , saldo
#	salir=True
	
	# Leer apuesta
	saldo,salir,apuesta=leer_apuesta(saldo,salir,apuesta)
				

# Ni gana ni pierde
if (saldo==100):
	print "\nGracias por venir"
else:
	# Ha perdido dinero
	if (saldo<100):
		print "\nCon pardillos como tu me forro"
	else:
		print "\nMe he quedado con tu cara, no vuelvas"


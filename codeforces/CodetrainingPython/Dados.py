import random

#Funcion Lanzar Dados
def lanzarDados():
	dado = input("Desea lanzar los dados? S/N\n")

	while dado=="S" or dado=="s":
		print("Hola mi perro")
		dado1 = random.randint(1,6)
		dado2 = random.randint(1,6)
		print("Dado 1 es %5d y dado 2 es %5d"%(dado1,dado2))
		print("la suma es %5d"%(dado1+dado2))	
		dado = input("Desea lanzar los dados de nuevo? S/N\n")
	
		
	else:
		#Si el valor no es s y es N lanza de nuevo los dados, sino es comando invalido
		if(dado=="N" or dado =="n"):
			print("Bye!")
			lanzarDados()
		else:
			print("comando invalido")

def saludarMarco():
	print("Hola gonorrea\n")

#Este if es el punto de entrada del programa y solo llama lanzar dados
if __name__ == '__main__':
	#Llamar la funcion saludar a Marco
	saludarMarco()
	#Llamar la funcion lanzar dados
	lanzarDados()
	
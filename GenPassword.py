import random 
from pystyle import *

System.Title('GenPassword')


banner = """
 ▄▀▀▀▀▄   ▄▀▀█▄▄▄▄  ▄▀▀▄ ▀▄      ▄▀▀▄▀▀▀▄  ▄▀▀█▄   ▄▀▀▀▀▄  ▄▀▀▀▀▄  ▄▀▀▄    ▄▀▀▄  ▄▀▀▀▀▄   ▄▀▀▄▀▀▀▄  ▄▀▀█▄▄  
█        ▐  ▄▀   ▐ █  █ █ █     █   █   █ ▐ ▄▀ ▀▄ █ █   ▐ █ █   ▐ █   █    ▐  █ █      █ █   █   █ █ ▄▀   █ 
█    ▀▄▄   █▄▄▄▄▄  ▐  █  ▀█     ▐  █▀▀▀▀    █▄▄▄█    ▀▄      ▀▄   ▐  █        █ █      █ ▐  █▀▀█▀  ▐ █    █ 
█     █ █  █    ▌    █   █         █       ▄▀   █ ▀▄   █  ▀▄   █    █   ▄    █  ▀▄    ▄▀  ▄▀    █    █    █ 
▐▀▄▄▄▄▀ ▐ ▄▀▄▄▄▄   ▄▀   █        ▄▀       █   ▄▀   █▀▀▀    █▀▀▀      ▀▄▀ ▀▄ ▄▀    ▀▀▀▀   █     █    ▄▀▄▄▄▄▀ 
▐         █    ▐   █    ▐       █         ▐   ▐    ▐       ▐               ▀             ▐     ▐   █     ▐  
          ▐        ▐            ▐                                                                  ▐        

"""
print(Colorate.Vertical(Colors.red_to_yellow, banner))

print(Col.blue + "1- Mot de passe normal : 8 caractères , contenant lettres majuscules et minuscules avec chiffres 2- Mot de passe sécurisé : Plus de 8 caractères contenant lettres majuscules et minuscules , avec chiffres et caractères spéciaux")
level = input("Choisissez une option : ")
def gen():
	chars = "abcdefghijklmnopqrsuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
	
	password = ''
	
	for i in range(8):
		password = f"{password}{random.choice(chars)}"		

	print(f"Mot de passe : {password}")
	
	with open("password.txt", "a+") as file:
		file.write(f"Mot de passe : {password}\n")
		file.close()

	print("\nVotre mot de passe est stocké dans le fichier password.txt")

def gen2():
		chars = "abcdefghijklmnopqrsuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789,?;.:/!§%#@"
	
		password = ''

		for i in range(16):
			password = f"{password}{random.choice(chars)}"		

		print(f"Mot de passe : {password}")
	
		with open("password.txt", "a+") as file:
			file.write(f"Mot de passe : {password}\n")
			file.close()

		print("\nVotre mot de passe est stocké dans le fichier password.txt")

if level == '1':
	gen()

if level == '2':
	gen2()
 
 
 
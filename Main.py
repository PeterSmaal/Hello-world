from Config import Config
import getpass
class Main:
	def __init__(self):
		self.config = Config()
		print("Welcome to PyChat V0.5")
		self.command = input("To Login/Register type Login/Register -> ")

		if self.command.lower() == "register":
			username = input("Please fill in a Username -> ")
			password = getpass.getpass("Please fill in a password -> ")
			mail = input("Please fill in your e-Mail -> ")
			self.register = True
			while self.register:
				if username != "":
					if password != "":
						if mail != "":
							self.config.register(username, password, mail)
							self.register = False
							self.config.login(username, password)
						else:
							mail = input("Please fill in your e-Mail -> ")
					else:
						password = getpass.getpass("Please fill in a password -> ")
				else:
					username = input("Please fill in a username -> ")

		elif self.command.lower() == "login":
			username = input("Username -> ")
			password = getpass.getpass("Password -> ")
			if self.config.login(username, password):
				

			
start = Main()



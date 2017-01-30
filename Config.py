import pymysql
class Config:
	def __init__(self):
		self.conn = pymysql.connect(host = 'localhost', user = 'root', password = '', db = 'game', charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
		self.a = self.conn.cursor()

	def register(self, username, password, mail):
			self.qry = 'INSERT INTO users (username, password, mail) VALUES(\"'+ username + '\", \"' + password + '\", \"' + mail + '\")'
			self.a.execute(self.qry)
			if(self.conn.commit()):
				return True
			else:
				return False

	def login(self, username, password):
		self.qry = 'SELECT password FROM users WHERE username = \"' + username + '\"'
		self.a.execute(self.qry)

		for row in self.a:
			temp = row

		if temp['password'] == password:
			print(temp['password'])
			return True
		else:
			return False
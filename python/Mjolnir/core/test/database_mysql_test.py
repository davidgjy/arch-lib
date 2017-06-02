from ..database.mysql.mysql_db import MySqlDb

# test mysql db
class MySqlDbTest:
	def __init__(self):
		db = MySqlDb()
		self.result = "Module Name: " + db.name
	def run(self):
		print(self.result)






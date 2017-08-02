from func import *

with db:
	for i in db.execute("SELECT * FROM note"):
		print(i)
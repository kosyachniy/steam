from func import *

db.execute("SELECT * FROM note")
for i in db.fetchall():
	print(i)

auth.commit()
auth.close()
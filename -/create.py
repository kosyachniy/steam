from func import *

db.execute("CREATE TABLE note (id int, name text, price real, count int)")

auth.commit()
auth.close()
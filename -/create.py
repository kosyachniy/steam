from func import *

db.execute("CREATE TABLE note (id int, name text, normal real, sale real, count int)")

auth.commit()
auth.close()
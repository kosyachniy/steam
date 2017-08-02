from func import *

while True:
	db.execute("SELECT * FROM note WHERE count>0")
	for i in db.fetchall():
		#API
		'''
		page=requests.get(i[1]).text
		soup=BeautifulSoup(page, 'lxml') #, 'html5lib'

		try:
			span=soup.find('table', class_='market_commodity_orders_table')
		except:
			print('Error!')
			time.sleep(600)
		else:
			print(span)
		'''
		time.sleep(5)
	time.sleep(300)

auth.commit()
auth.close()
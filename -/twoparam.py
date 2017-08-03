from func import *

while True:
	with db:
		for i in db.execute("SELECT * FROM note"): # WHERE count>0
			page=requests.get(i[1]).text
			page=page[page.find('var line1=[')+11:]
			data=[page[0:35]]
			page=page[36:]
			print(page[0:5])
			while page[0]=='[':
				print(page[0:36])
				page=page[37:]
			'''
			soup=BeautifulSoup(page, 'lxml') #, 'html5lib'

			try:
				span=soup.find('table', class_='market_commodity_orders_table')
			except:
				print('Error!')
				time.sleep(600)
			else:
				print(span)
			'''
			time.sleep(500)
	time.sleep(300)
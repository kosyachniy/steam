from func import *

su=-235.7
while True:
	with db:
		for i in db.execute("SELECT * FROM note WHERE count>0"):
			page=requests.get('http://steamcommunity.com/market/search?q='+names(i[1])).text
			soup=BeautifulSoup(page, 'html5lib')

			try:
				span=soup.find('span', class_='market_table_value normal_price')
				normal=float(span.find('span', class_='normal_price').contents[0][1:-4])
				sale=float(span.find('span', class_='sale_price').contents[0][1:-4])
			except:
				print('Error!')
				time.sleep(300)
			else:
				print(normal, sale, i[2])

				price=i[2] 
				if sale>=price+0.1 or sale<=price-0.6:
						delta=str(round(sale-price, 2))
						if delta[0]!='-':
							delta='+'+delta
						su+=0.85*sale

						db.execute("UPDATE note SET count=0 WHERE name=(?)", (i[1],))
						send(140420515, 'Продать! %s\n%s\nΔ %s$\n∑ %f$' % (names([1]), i[1], delta, round(su, 2)))

			time.sleep(1)
	time.sleep(300)
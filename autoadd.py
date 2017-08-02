from func import *

su=793.46 #0
while True:
	for s in range(10):
		page=requests.get('http://steamcommunity.com/market/search?q=#p'+str(s)+'_popular_desc').text
		soup=BeautifulSoup(page, 'lxml') #, 'html5lib')

		try:
			table=soup.find('div', id='searchResultsRows')
			a=table.find_all('a', class_='market_listing_row_link')
		except:
			print('Error!')
			time.sleep(600)
		else:
			for i in a:
				href=i.get('href')
				span=i.find('span', class_='normal_price')
				normal=float(span.find('span', class_='normal_price').contents[0][1:-4])
				sale=float(span.find('span', class_='sale_price').contents[0][1:-4])

				with db:
					t=False
					for i in db.execute("SELECT * FROM note WHERE name=(?)", (href,)):
						price=i[2]
						count=i[3]
						if count>0 and (sale>=price+0.1 or sale<=price-0.6):
							delta=str(round(sale-price, 2))
							if delta[0]!='-':
								delta='+'+delta
							su+=0.85*sale
							db.execute("UPDATE note SET count=0 WHERE name=(?)", (href,))
							send(140420515, 'Продать! %s\n%s\nΔ %s$\n∑ %f$' % (names(href), href, delta, round(su, 2)))
						t=True
						break
					if t:
						continue

					'''
					db.execute("INSERT INTO note (name, price, count) VALUES (?, ?, 1)", (href, round(normal, 2)))
					su-=normal
					send(140420515, 'Купить! %s\n%s\n∑ %f$' % (names(href), href, round(su, 2)))
					'''

		time.sleep(5)
	time.sleep(300)
from func import *

while True:
	#Считать базу
	#Пропарсить для каждого страницу
	#Продать / ничего
	'''
	for s in range(10):
		page=requests.get('http://steamcommunity.com/market/search?q=#p'+str(s)+'_popular_desc').text
		soup=BeautifulSoup(page, 'lxml') #, 'html5lib'

		try:
			table=soup.find('div', id='searchResultsRows')
			a=table.find_all('a', class_='market_listing_row_link')
		except:
			print('Error!')
			time.sleep(600)
		else:
			for i in a:
				href=unquote(i.get('href'))
				span=i.find('span', class_='normal_price')
				normal=float(span.find('span', class_='normal_price').contents[0][1:-4])
				sale=float(span.find('span', class_='sale_price').contents[0][1:-4])

				#Сделать парсинг тех, которые есть в базе, но нет в тренде
				db.execute("SELECT * FROM note WHERE name=(?)", (href,))
				try:
					price=db.fetchone()[3]
				except:
					db.execute("INSERT INTO note VALUES (%d, '%s', '%f', '%f', 0)" % (k, href, normal, sale))
					su-=sale
					send(140420515, 'Купить!\n%s\n%f' % (href, su))
				else:
					#print(price, sale, sale-price)
					if sale>=price+0.1 or sale<=price-0.5:
						#print(price, sale)
						delta=str(sale-price)
						if delta[0]!='-':
							delta='+'+delta
						su+=sale-price
						send(140420515, 'Продать!\n%s$\n%f' % (delta, su))
		time.sleep(5)
		'''
	time.sleep(300)

auth.commit()
auth.close()
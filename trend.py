from func import *

url='http://steamcommunity.com/market/search?q=#p'

su=0
for s in range(10):
	page=requests.get(url+str(s)+'_popular_desc').text
	soup=BeautifulSoup(page, 'lxml')

	table=soup.find('div', id='searchResultsRows')
	a=table.find_all('a', class_='market_listing_row_link')

	for i in a:
		href=i.get('href')
		print(href)
		span=i.find('span', class_='normal_price')
		normal=float(span.find('span', class_='normal_price').contents[0][1:-4])
		sale=float(span.find('span', class_='sale_price').contents[0][1:-4])
		print(normal, sale)
		print('--------------------')
		
		if normal-sale<0.4:
			su+=sale
			with db:
				db.execute("INSERT INTO note (name, price, count) VALUES ('%s', %f, 1)" % (href, normal))
	time.sleep(1)

send(140420515, 'Купить!\n∑ %f$' % round(su, 2))
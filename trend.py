from func import *

url='http://steamcommunity.com/market/search?q=#p'

k=0
su=0
for s in range(10):
	page=requests.get(url+str(s)+'_popular_desc').text
	soup=BeautifulSoup(page, 'lxml')

	table=soup.find('div', id='searchResultsRows')
	a=table.find_all('a', class_='market_listing_row_link')

	for i in a:
		href=unquote(i.get('href'))
		print(href)
		span=i.find('span', class_='normal_price')
		normal=float(span.find('span', class_='normal_price').contents[0][1:-4])
		sale=float(span.find('span', class_='sale_price').contents[0][1:-4])
		print(normal, sale)
		print('--------------------')

		k+=1
		su+=sale
		db.execute("INSERT INTO note VALUES (%d, '%s', '%f', 0)" % (k, href, sale))
	time.sleep(1)

auth.commit()
auth.close()
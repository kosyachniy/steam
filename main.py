import requests, time, json
from bs4 import BeautifulSoup
from urllib.request import unquote

url='http://steamcommunity.com/market/search?q=#p'

for s in range(10):
	page=requests.get(url+str(s)+'_popular_desc').text
	soup=BeautifulSoup(page, 'lxml')
	table=soup.find('div', id='searchResultsRows')
	a=table.find_all('a', class_='market_listing_row_link')
	for i in a:
		print(unquote(i.get('href')))
		span=i.find('span', class_='normal_price')
		normal=span.find('span', class_='normal_price')
		sale=span.find('span', class_='sale_price')
		print(normal.contents[0][1:-4], sale.contents[0][1:-4])
		print('--------------------')
	time.sleep(1)
from func import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome('./chromedriver')

#elem=driver.find_element_by_class_name('global_action_link')
#elem.click()

driver.get('https://steamcommunity.com/login/home/')
with open('set.txt', 'r') as file:
	s=json.loads(file.read())['steamlog']
	driver.find_element_by_id('steamAccountName').send_keys(s[0])
	driver.find_element_by_id('steamPassword').send_keys(s[1])
	#driver.find_element_by_id('remember_login').click()
	driver.find_element_by_id('SteamLogin').click()

	#browser=webdriver.Chrome('./chromedriver')
	#browser.get("mail.ru")

time.sleep(30)
#driver.find_element_by_class_name('auth_button leftbtn').click()

#time.sleep(5)
#driver.find_element_by_id('success_continue_btn').click()

driver.get("http://steamcommunity.com/market/")
driver.find_element_by_class_name('item_market_action_button_contents').click()
time.sleep(10)
driver.find_element_by_id('730_2_8695061953').click()
driver.find_element_by_id('item_market_action_button item_market_action_button_green').click()
time.sleep(10)

price=10
driver.find_element_by_id('market_sell_currency_input').send_keys(price)
driver.find_element_by_id('market_sell_dialog_accept_ssa').click()
driver.find_element_by_id('market_sell_dialog_accept').click()
driver.find_element_by_id('market_sell_dialog_ok').click()

while True: pass

'''
su=0
while True:
	with db:
		for i in db.execute("SELECT * FROM note WHERE count>0"):
			page=requests.get('http://steamcommunity.com/market/search?q='+names(i[1])).text
			soup=BeautifulSoup(page, 'lxml') #, 'html5lib')

			try:
				span=soup.find('span', class_='market_table_value normal_price')
				normal=float(span.find('span', class_='normal_price').contents[0][1:-4])
				sale=float(span.find('span', class_='sale_price').contents[0][1:-4])
			except:
				print('Error!')
				#time.sleep(300)
			else:
				print(normal, sale, i[2])

				price=i[2] 
				if sale>=price+0.1 or sale<=price-0.6:
						delta=str(round(sale-price, 2))
						if delta[0]!='-':
							delta='+'+delta
						su+=0.85*sale

						#db.execute("UPDATE note SET count=0 WHERE name=(?)", (i[1],))
						#send(140420515, 'Продать! %s\n%s\nΔ %s$\n∑ %f$' % (names([1]), i[1], delta, round(su, 2)))

						#elem=driver.find_element_by_classname('item_market_action_button item_market_action_button_green')
						#print(elem)
						#elem.send_keys("pycon")
						#elem.send_keys(Keys.RETURN)

			time.sleep(1)
	time.sleep(300)
'''
driver.close()
import requests, time, json, sqlite3, vk_api
from bs4 import BeautifulSoup
from urllib.request import unquote

with open('set.txt', 'r') as file:
	s=json.loads(file.read())
	vk=s['vk']
	steam=s['steam']

#VK
vk=vk_api.VkApi(token=vk)
vk.auth()

send=lambda user, cont, img=[]: vk.method('messages.send', {'user_id':user, 'message':cont, 'attachment':','.join(img)})

#SQLite
db=sqlite3.connect('1.db')

'''
#Steam
from steam import WebAPI, SteamClient

api=WebAPI(key=steam)
'''
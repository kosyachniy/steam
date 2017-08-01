import requests, time, json, sqlite3, vk_api
from bs4 import BeautifulSoup
from urllib.request import unquote

with open('set.txt', 'r') as file:
	vk=vk_api.VkApi(token=json.loads(file.read())['token'])
vk.auth()

auth=sqlite3.connect('1.db')
db=auth.cursor()

send=lambda user, cont, img=[]: vk.method('messages.send', {'user_id':user, 'message':cont, 'attachment':','.join(img)})
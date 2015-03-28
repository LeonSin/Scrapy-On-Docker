# -*- coding:utf-8 -*-

import requests
import bs4

session = requests.session()

column = 10

for index in range(column):
	url  = 'http://www.dockerone.com/article/' + str(index + 1)
	response = session.get(url)
	if(response.status_code == 200):
		soup  = bs4.BeautifulSoup(response.text)
		title = soup.select('title')[0].get_text()
		print title + '  ' + response.url
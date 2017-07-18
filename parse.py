import requests
import urllib
from bs4 import BeautifulSoup

def Getting_request(data):
	params = urllib.urlencode(data)
	url = 'http://wsprnet.org/olddb?' + params #findcall=ZL1WJQ&limit=1'
	r = requests.get(url)
	html_doc = r.text
	soup = BeautifulSoup(html_doc, "html.parser")
	for i, row in enumerate(soup.find_all('tr')):
		if i != 0 and i!= 1 and i != 2 and i != 3:
			print(row.get_text().encode('utf-8'))

data = {} 
field = ''
while field != 'Done':
	field = raw_input('Enter the parameters : ')
	if field == 'Done':
		break
	value = raw_input('Enter parameter value : ')
	data[field] = value
Getting_request(data)
import requests, re
from bs4 import BeautifulSoup

r = requests.get(str("https://abilligeobillige.000webhostapp.com/ezpz"))
soup = str(BeautifulSoup(r.text, 'html.parser'))

print(str(soup))
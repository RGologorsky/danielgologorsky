import requests

web_addr = "https://www.healthgrades.com/physician/dr-daniel-gologorsky-y9qfc2z"

page = requests.get("web_addr")
print(page)

from bs4 import BeautifulSoup
soup = BeautifulSoup(page.content, 'html.parser')

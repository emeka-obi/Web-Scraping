import bs4
import lxml
import requests

request = requests.get("https://en.wikipedia.org/wiki/Grace_Hopper")

# print(request.text)

soup = bs4.BeautifulSoup(request.text, "lxml")

content = soup.select('.toctext')
print(content[0]['span'])
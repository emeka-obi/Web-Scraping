import requests
import bs4
import lxml

result = requests.get("https://toscrape.com/")
soup  = bs4.BeautifulSoup(result.text, "lxml")

content = soup.select('div')[0]

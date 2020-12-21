import bs4
import lxml
import requests

authors_list = []
Quote_list = []
res = requests.get("https://quotes.toscrape.com/")
soup = bs4.BeautifulSoup(res.text, "lxml")
authors = soup.select(".author")
for author in authors:
   authors_list.append(author.getText())
# print(authors_list)

quotes = soup.select(".text")
for quote in quotes:
    Quote_list.append(quote.getText())
print(Quote_list)
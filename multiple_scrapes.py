import bs4
import lxml
import requests

#using .format conveniently allows you to change the string
base_url = "https://books.toscrape.com/catalogue/page-{}.html"
# res = requests.get(base_url.format(1))
# #using beautiful soup
# soup = bs4.BeautifulSoup(res.text, "lxml")
# product_pod = soup.select(".product_pod")
# example = product_pod[0]
# print(type(product_pod))
# print(type(example))
# print(example.select(".star-rating.Two"))
# print(example.select("a")[1]['title'])
# count = 0
# two_star_title = []
# for i in range(1,51):
#     new_url = base_url.format(i)
#     res = requests.get(new_url)

#     soup = bs4.BeautifulSoup(res.text, "lxml")
#     books = soup.select(".product_pod")

#     for book in books:
#         if len(book.select(".start-rating.Two")) != 0:
#             two_star_title.append(book.select('a')[1]['title'])

# print(two_star_title)

two_star_titles =  []
for n in range(1,51):

    scrape_url = base_url.format(n)
    res = requests.get(scrape_url)
    
    soup = bs4.BeautifulSoup(res.text,"lxml")
    books = soup.select(".product_pod")
    
    for book in books:
        if len(book.select('.star-rating.Two')) != 0:
            two_star_titles.append(book.select('a')[1]['title'])

print(two_star_titles)
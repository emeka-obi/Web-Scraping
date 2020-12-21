import bs4
import lxml
import requests

#look for image
request = requests.get("https://en.wikipedia.org/wiki/Deep_Blue_(chess_computer)")
# print(request.text)
# print(request.content)
soup = bs4.BeautifulSoup(request.text, "lxml")


content = soup.select('.thumbimage')
# print(content)
#specify its location
computer = soup.select('.thumbimage')[0]
print(computer['src'])
"""https://upload.wikimedia.org/wikipedia/commons/6/6f/Kasparov_Magath_1985_Hamburg-2.png"""
#send a request to the image
image_link = requests.get("https://upload.wikimedia.org/wikipedia/commons/6/6f/Kasparov_Magath_1985_Hamburg-2.png")

#open the image, give it permissions and then save it to your computer
f = open('awesome_image.png','wb')
f.write(image_link.content)

f.close()
import requests
import bs4
import lxml


output_dict = {}
new_list = []
result = requests.get("http://www.example.com")
soup  = bs4.BeautifulSoup(result.text, "lxml")

"""lsml is used to iterate through the result.txt to figure out what is a css file, html file or .js file
    Beautiful soup goes through restults.txt and helps to easily parse it for useful information
"""
# print(soup.select("title")[0].getText())
paragraph = soup.select("p")
edited_paragraph = paragraph[0].getText().split()
for words in edited_paragraph:
    if words not in output_dict:
        output_dict[words] = 1
    else:
        output_dict[words] += 1

print(output_dict)

"""You can do alot of manipulations after converting the type"""


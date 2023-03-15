import requests
from bs4 import BeautifulSoup
import os
import re


url_link = 'https://en.wikipedia.org/wiki/List_of_states_and_territories_of_the_United_States'
res = requests.get(url_link).text

doc = BeautifulSoup(res,'html.parser')

# print(doc.prettify())
# print(doc)

# print(doc.contents[:100])


# fetching the data using the class name
# res = doc.find(id='content')


# res = doc.find(class_ = "firstHeading")
# # print(res)

# res = doc.find(id = "content")
# data = []
# for i in res:
#     data.append(res.find("h2"))


# # Find using the specific text
# res = doc.find_all(text = "California")
# print(res)


# we can search using by passing the list of ele to be searched 

# res = doc.find_all(["meta","link"])

# # print(res)
# l = []
# for i in doc.find_all(text = re.compile("1788")):
#     l.append(i)

#select used to run a CSS selector against a parsed document and return all the matching elements. 
# print(doc.select("title"))
# print(doc.select("footer"))

# print(doc.select(".vector-menu-content"))


# print(doc.select("a[href]"))


# with open(os.path.join('/home/nagaraj/pythonLearn/pyproject/python/Web_Scrap','regular_exp.html'),'w') as d:
#     d.write(str())



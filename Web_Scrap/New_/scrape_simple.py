from bs4 import BeautifulSoup
import requests


with open('/home/nagaraj/pythonLearn/pyproject/python/Web_Scrap/New_/simple.html') as html_file:
    soup = BeautifulSoup(html_file,'lxml')

# print(soup.prettify())

# this fetches the first tags available
# data = soup.div.text


# data  = soup.find(class_ = "footer")

# data  = soup.find('div',class_ = "footer")
# print(data)

for article in  soup.find_all('div',class_ = 'article'):
    headline = article.h2.a.text
    print(headline)

    summary = article.p.text
    print(summary)
    print("==================")
    
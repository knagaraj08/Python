import requests
from bs4 import BeautifulSoup
import os,re

url_link = "https://webscraper.io/test-sites/e-commerce/allinone"

res = requests.get(url_link).text

doc = BeautifulSoup(res,'html.parser')

with open(os.path.join('/home/nagaraj/pythonLearn/pyproject/python/Web_Scrap','E-Comm.html'),'w') as f:
    f.write(str(doc))
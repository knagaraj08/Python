
import requests
from bs4 import BeautifulSoup

page  = requests.get("https://codedamn.com")

soup = BeautifulSoup(page.content,'html.parser')
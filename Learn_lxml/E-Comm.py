from lxml import html
import requests

page = requests.get("https://webscraper.io/test-sites/e-commerce/allinone")

tree = html.fromstring(page.content)

prices = tree.xpath('//div[@class="col-sm-4 col-lg-4 col-md-4"]/div/div[1]/h4[1]/text()')
print(prices)
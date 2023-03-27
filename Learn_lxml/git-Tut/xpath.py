from lxml import html

with open('/home/nagaraj/pythonLearn/pyproject/python/Learn_lxml/git-Tut/input.html') as f:
    html_str = f.read()

tree = html.fromstring(html_str)
p = tree.xpath('//p/text()')

for i in p:
    print(i)
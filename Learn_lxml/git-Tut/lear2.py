from lxml import etree

tree = etree.parse('input.html')
el = tree.getroot()
# etree.dump(el)

# print(el)

para = el.findall('body/p')
for e in para:
    etree.dump(e)
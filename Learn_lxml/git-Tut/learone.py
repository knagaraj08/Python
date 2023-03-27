from lxml import etree

root = etree.Element("html")

head = etree.SubElement(root,"head")
title = etree.SubElement(head,"title")
title.text = "Page Title"


body = etree.SubElement(root,"body")
heading = etree.SubElement(body,"h1",style="font-size:20pt", id="head")
heading.text = "Hey!S"

para = etree.SubElement(body,"p",style="font-size:20pt", id="firstPara")
para.text = "Hello NK"


para = etree.SubElement(body,"p",style="font-size:20pt", id="secondPara")
para.text = "This HTML is XML Compliant!"

# etree.dump(root)


with open('/home/nagaraj/pythonLearn/pyproject/python/Learn_lxml/git-Tut/input.html','wb') as f:
    f.write(etree.tostring(root,pretty_print=True))

    
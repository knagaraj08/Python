import xml.etree.ElementTree as ET


# passing xml file as a Parameter
mytree = ET.parse('/home/nagaraj/pythonLearn/pyproject/python/Learn_lxml/sample.xml')
myroot = mytree.getroot()

# print(myroot.tag)


# print(myroot[0].attrib)  #the attrib gives the result in the dictionary form


# for i in myroot[0]:
#     print(i.tag,i.attrib)

# for i in myroot[0]:
#     print(i.text)

# for i in myroot.findall('book'):
#     title = i.find('title').text
#     price = i.find('price').text
#     print(title,price)


# # this is to add more content to the existing description tag and writing it to a new File
# for i in myroot.iter('description'):
#     val = str(i.text)+"Added Extra"
#     i.text = str(val)
#     i.set("Description","Yes")

# mytree.write('new.xml')


ET.SubElement(myroot[0],"Deliverable")  #this add a new tag in the xml documnet

for i in myroot.iter('Deliverable'):
    val = "Yes"
    i.text = str(val)

mytree.write("Added_new_Tag.xml")

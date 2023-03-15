import requests
from bs4 import BeautifulSoup
import os


url_link = 'https://en.wikipedia.org/wiki/List_of_states_and_territories_of_the_United_States'
res = requests.get(url_link).text

doc = BeautifulSoup(res,'html.parser')



my_tab = doc.find("table",class_ = "wikitable sortable plainrowheaders")


# with open(os.path.join('/home/nagaraj/pythonLearn/pyproject/python/Web_Scrap','Table.html'),'w') as d:
#     d.write(str(my_tab))




table_head = my_tab.find_all('th')
states = []

for i in table_head:
    anchor_tag = i.find_all("a")
    for j in anchor_tag:
        states.append(j.string)

f_states = states[9:]

final_list_states = []
for i in f_states:
    if len(i)>3:
        final_list_states.append(i)


# print(final_list_states)

# All div's in the table

all_divs = my_tab.find_all("div")
population = []
for i in all_divs:
    population.append(i.string)

# print(population)

population_final  = []

for i in population:

    if len(i)>3:
        population_final.append(i.string)

print(population_final)


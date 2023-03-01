import requests



# res = requests.get('https://codedamn.com')

# print(res.text)
# print(res.status_code)


res = requests.get('https://codedamn-classrooms.github.io/webscraper-python-codedamn-classroom-website/')

res_txt = res.text

res_status = res.status_code

print(res_txt,res_status)


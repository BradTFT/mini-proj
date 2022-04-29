# this is gonna be my first real attempt in webscraping while following a tutorial

import requests
from bs4 import BeautifulSoup

#this is with requests on a webpage
url = 'https://www.squidindustries.co/collections/all-trainers/products/krake-raken-trainer-v2-5?variant=36643470246050'

result = requests.get(url)
doc = BeautifulSoup(result.text, 'html.parser')

prices = doc.find_all(text='$')
#! error 2 README.md (line13)
parent = prices[0].parent
strong = parent.find('strong')

print(strong.string)





#finding within local html file
'''
with open('index.html', 'r') as f:
    doc = BeautifulSoup(f, 'html.parser')

tag = doc.find('')
print(tag)
'''
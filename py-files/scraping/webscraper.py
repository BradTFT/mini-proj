
#! not a fan of this tutorial; super complex
import requests
from bs4 import BeautifulSoup
import re

gpu = input('product >>> ')

url = f'https://www.newegg.com/p/pl?d={gpu}&N=4131'
page = requests.get(url).text
doc = BeautifulSoup(page, 'html.parser')

page_text = doc.find(class_='list-tool-pagination-text').strong
pages = int(str(page_text).split('/')[-2].split('>')[-1][:-1])

#! i found a yt short regarding out of index range issues using for in range. im going to try this 
#! and see if it fixes the issue with this script.

"""old:
for page in range(1, pages, +1)"""
#! works
#new:
list2 = 1, pages, +1

for page in list2:
    url = f'https://www.newegg.com/p/p1?d={gpu}&N=4131&page={page}'
    page = requests.get(url).text
    doc = BeautifulSoup(page, 'html.parser')
    
    #! new issue: README.md Error 5
    div = doc.find(class_="item-cells-wrap border-cells items-grid-view four-cells expulsion-one-cell")
    items = div.find_all(text=re.compile(gpu))

    for item in items:
        print(item)

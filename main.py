from bs4 import BeautifulSoup

import requests

import collections.abc
#hyper needs the four following aliases to be done manually.
collections.Iterable = collections.abc.Iterable
collections.Mapping = collections.abc.Mapping
collections.MutableSet = collections.abc.MutableSet
collections.MutableMapping = collections.abc.MutableMapping

from hyper.contrib import HTTP20Adapter



product = input("input product: ")

location = "sankt_peterburg_i_lo"
cathegory = "tovary_dlya_kompyutera/" \
"komplektuyuschie/kontrollery-ASgBAgICAkTGB~pm7gnsZw"


links_container = []


ref = "https://www.avito.ru/"
url = ref + location + "/" + cathegory + "?&q=" + product
url = ref + location+"/"+cathegory+"?cd=1&q=" + product



s = requests.Session()
s.mount('https://', HTTP20Adapter())

def evil(session, url, num):
    print("<===========================================>")
    request = session.get(url + "p=" + str(num))

    bs = BeautifulSoup(request.text, "html.parser")

    all_link = bs.find_all("a", "iva-item-sliderLink-uLz1v")

    for link in all_link:
        links_container.append(ref+ link['href'])
        #print(ref+ link['href'])

    #pager = bs.find_all("a", "pagination-page")
    if len(all_link) > 0:
        num += 1
        evil(session, url, num)
    
    



evil(s, url, 1)


request = s.get(url)
"""
bs = BeautifulSoup(request.text, "html.parser")

all_link = bs.find_all("a", "iva-item-sliderLink-uLz1v")

for link in all_link:
    links_container.append(ref+ link['href'])
    print(ref+ link['href'])
"""

for link in links_container:
    print("----------------------------------------------\n")
    print(link)
    print("\n----------------------------------------------")

    

print(len(links_container))


print(request.status_code)

print("hello, my dears!!!!!")
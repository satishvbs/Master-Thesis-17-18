#web scrapping to dextract all main tiles form the wikipedia page of machine leraing exmaple:overview
#Machine Learning Tast etc

import bs4
import requests

request_obj = requests.get('https://en.wikipedia.org/wiki/Machine_learning')
soup_obj = bs4.BeautifulSoup(request_obj.content,'lxml')
#soup object to store content of req obj into lxml format 

#print(soup)

for i in soup_obj.select('#toc'):
    #classes are accesed using dot '.' while other using # or $
    print(i.text)
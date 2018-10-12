#This script fetch the Global Stechiometry of protein structure of asymetrical uni
import requests

from bs4 import BeautifulSoup

import pandas as pd

import os

print(os.getcwd())

# Reading file form the directory
# Index_col is to print index as per our wish.its not mandatory though

data = open('E:/Python Thesis/Data-Download/Xcel Files/Filter 1-Transporters-List-7_oct.csv','r')
data.readline()

#for lines in data:
url = 'https://www.rcsb.org/structure/1KPL'
page = requests.get(url)



# construct soup object
soup = BeautifulSoup(page.content, 'html.parser')
#print(soup.prettify())

# extract table element and collect all <tr> elements
containers = soup.find("div", attrs={"id": "maincontentcontainer"})

carousel = containers.find("div",attrs={"class":"carousel-footer"}).get_text()
print(carousel[167:])
'''
carousel_text = carousel.get_text()
print(carousel_text)
carousel_length = len(carousel_text)
print(carousel_text[167:])

'''








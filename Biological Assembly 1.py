#This script fetch the Global Stechiometry of protein structure from Biological Assembly one.Here
import requests
from bs4 import BeautifulSoup
import os

# Reading file form the directory
data = open('E:/Python Thesis/Data-Download/Xcel Files/Filter 1-Channels-LINK-7_oct.txt','r')
lines = data.read().splitlines()#without split all the links will pass together with'\n'. it give 400 erro
#lines = ['https://www.rcsb.org/structure/5tsi']
#url = 'https://www.rcsb.org/structure/2itc'
out = ""

out_file = open("hmer-channel.txt", "w")


for line in lines:
    pdb_ID = line[-4:]

    #print(line)
    page = requests.get(line)
# construct soup object
    #print(page.status_code)
    soup = BeautifulSoup(page.content, 'html.parser')
# extract table element and collect all <tr> elements
    containers = soup.find("div", attrs={"id": "maincontentcontainer"})
    carousel_Bio1 = containers.find("div", attrs={"id":"structureimagesection"})
    bio_stochiometry = carousel_Bio1.findChildren("div")[-1]

    text = bio_stochiometry.get_text().strip()
    #print(text)
    ind = text.rfind('H')
    if ind == -1:
        ind = text.rfind('M')
    assert ind != -1
    hmer = text[ind:]
    space_ind = [i for i, c in enumerate(hmer) if ord(c) == 160]#160 is no breakable space charater in web page
    index = 0
    if len(space_ind) > 1:
        index = 1
    currnt_out = pdb_ID + "\t" +hmer[:space_ind[index]]+'\n'
    #print(currnt_out)
    out = out + currnt_out

out_file.write(out)
out_file.close()



'''space_n = 3
count = 0
for i, s in enumerate(hmer):
    if s == ' ':
        count = count + 1
        if count == space_n:
            break
print(ord(hmer[22]))
'''



'''
'''
#this dont work in loop..its give 400 bad request
'''

for lines in data:
    url = lines
    print(url)
    pdb_id =url[-5:]
    print(pdb_id)
    page = requests.get(url)
    # construct soup object
    soup = BeautifulSoup(page.content, 'html.parser')
    print(page)
    # extract table element and collect all <tr> elements
    containers = soup.find("div", attrs={"id": "maincontentcontainer"})
    carousel = containers.find("div", attrs={"class":"carousel-footer"})
    text = carousel.get_text().strip()
    #print(text)


'''
'''

for i in data:
    print(i.strip('\n'))

'''






#proteinTable = soup.find("div", attrs={"id": "table_macromolecule-protein-entityId-1"}).find("tbody")
#rows = proteinTable.find_all("tr")
#data = rows.find("td")




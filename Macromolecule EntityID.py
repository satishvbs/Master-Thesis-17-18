#This script fetch UniProtKB ID and link form each PDB page form the list
import requests
from bs4 import BeautifulSoup


# Reading file form the directory
#data = open('E:/Python Thesis/Data-Download/Xcel Files/Filter 1-Channels-LINK-7_oct.txt','r')
#lines = data.read().splitlines()
#lines = ['https://www.rcsb.org/structure/5tsi']
url = 'https://www.rcsb.org/structure/1k4c'

#out = ""
#out_file = open("hmer-channel.txt", "w")


#for line in lines:
    #pdb_ID = line[-4:]

    #print(line)

page = requests.get(url)
# construct soup object
#print(page.status_code)
soup = BeautifulSoup(page.content, 'html.parser')
#print(soup)
table1_row1 = soup.find(id="macromolecule-entityId-1-rowDescription").contents[0]
print(table1_row1.string)

table1_row1 = soup.find(id="macromolecule-entityId-1-rowDescription").contents[0]
table1_row1col2 = soup.find(id="macromolecule-entityId-1-rowDescription").contents[1]
print(table1_row1col2.string)
table2_row5 = soup.find(id="table_macromolecule-protein-entityId-3").find("tbody").contents[4].contents[0]
elem_a = table2_row5.find("span").find("a")
print(elem_a["href"])

table3_row5 = soup.find(id="table_macromolecule-protein-entityId-3").find("tbody").contents[4].contents[0]
elem_a = table2_row5.find("span").find("a")
print(elem_a.get_text())

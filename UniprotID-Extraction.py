#This script fetch UniProtKB ID and link form each PDB page form the list
import requests
from bs4 import BeautifulSoup


# Reading file form the directory
data = open('E:/Python Thesis/Data-Download/Xcel Files/Filter 1-Channels-LINK-7_oct-copy.txt','r')
lines = data.read().splitlines()
#lines = ['https://www.rcsb.org/structure/5tsi']
#url = 'https://www.rcsb.org/structure/4RDQ'

for line in lines:
    out = ''
    pdb_id = line[-4:]
    out = out + pdb_id
    page = requests.get(line)
# construct soup object
#print(page.status_code)
    soup = BeautifulSoup(page.content, 'html.parser')

    table_divs= soup.find("div",{"id":"MacromoleculeTable"}).contents
#print(table_divs)
    for table_div in table_divs:
        table_body = table_div.contents[0].find("tbody")
        span_tag = table_body.find("span", {"class": "label label-external"})
        if span_tag != None:
            out = out + '\t' + span_tag.find("a").string
        else:
            out = out + '\t' + 'NA'
        out = out + '\t' + table_body.contents[0].string
        out = out + '\t' + table_body.contents[2].contents[1].string
    print(out)


'''
for i in tables[:-1]:
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
'''
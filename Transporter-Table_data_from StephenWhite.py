
#This script fetch the required Transporters subfamilies row item i.e description and pdb name and link from Stephen white protein table
import requests
from bs4 import BeautifulSoup

url = 'http://blanco.biomol.uci.edu/mpstruc/#id_TRANSMEMBRANE_PROTEINS_ALPHAHELICAL:Adventitious_Membrane_Proteins_Alphahelical_Poreforming_Toxins'

# read locally or download using url
page = requests.get(url)
#page = open('E:/Python Thesis/Data-Download/stphenwhite.html', 'r').read()

# construct soup object
soup = BeautifulSoup(page.text, 'html.parser')

# extract table element and collect all <tr> elements
proteinTable = soup.find("table", attrs={"class":"aProteinTable"}).find("tbody")
rows = proteinTable.find_all("tr")

#end = len(rows) - 1
#for i, row in enumerate(rows):
#    if row.has_attr("id") and row["id"] == "f_3":
#        start = i + 1

start = 347
end = 1629
id_list = [72, 124, 40, 112, 104, 42, 43, 79, 88, 44, 70, 118, 45, 46, 47, 48, 49, 75, 50, 51, 52, 38]
'''
print(rows[1]["class"])
print(rows[1].has_attr("id"))
print(rows[12].extract())
'''

sf_found = False
out = ""
out_file = open("List-Transporters-7_oct.xls", "w",encoding="utf-8")

while start != end:
    if rows[start].has_attr("id"):
        cur_id = int(rows[start]["id"][3:])
        if cur_id in id_list:
            sf_id = str(cur_id) + "_3"
            sf_found = True
            out = rows[start].get_text().strip()
            out += '\n'
            #print(out)
            #out_file.write(out)
        else:
            sf_found = False
    elif sf_found:
        cols = rows[start].find_all("td")
        out = cols[0].find("strong").get_text().strip()
        out += "\t"
        out += cols[1].get_text().strip()
        out += "\t"
        out += cols[1].find("a")["href"]
        out += '\n'
        print(out)
        #out_file.write(out)
    start = start + 1
#out_file.close()
"""
for row in rows:
    if row.has_attr("id") and row["class"][0] == "sectionName":
        sub_family = row.get_text()
    elif row.has_attr("id") == False:
        cols = row.find_all("td")
        print(str(cols[0]) + "    " + str(cols[1]))
"""
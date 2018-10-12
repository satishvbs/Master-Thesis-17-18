import os
import requests
from bs4 import BeautifulSoup

txb = 'https://en.wiktionary.org/wiki/Appendix:Tocharian_B_Swadesh_list'
pt_old = 'https://en.wiktionary.org/wiki/Appendix:Old_Portuguese_Swadesh_list'

# get the web page & extract table
page = requests.get(pt_old)
soup = BeautifulSoup(page.text, 'html.parser')
table = soup.find("table", attrs={"class": "wikitable"})

words = []
EXPECTED_LENGTH = 207
COL_ID = 2

# Extract all rows except header in a table
for i, row in enumerate(table.find_all("tr")[1:]):
    words.append(row.find_all("td")[COL_ID].get_text())
    print(i)
    print(row)

# assert len(words) == EXPECTED_LENGTH
# print(words)
#This script fetches UniProtKB seuqnce from webpage form  links form  a text file

import requests
from bs4 import BeautifulSoup


# Reading file form the directory
data = open('E:/Python Thesis/Data-Download/Xcel Files/uniprot-old-id.txt','r')

#############################################
#This code is to make links of Uniprot IDS
http = "https://www.uniprot.org/uniprot/"
fasta = ".fasta"
links =""
for lines in data:
    line = lines.strip()
    new_link =http+line+fasta
    links =links +new_link+ '\n'
print(links)
outfile = open('Uniprot-LINKS-DEMO.txt', 'w')
outfile.write(links)
outfile.close()
#########################################################
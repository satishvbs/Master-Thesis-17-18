#12/102018
#This script fetch UniProtKB seq form web page (from given link page) and save it as .fasta file
import requests
from bs4 import BeautifulSoup


# Reading file form the directory
data = open('E:/Python Thesis/Data-Download/Xcel Files/Uniprot-LINKS-DEMO.txt','r')
lines = data.read().splitlines()
#lines = ['https://www.rcsb.org/structure/5tsi']
#url = 'https://www.uniprot.org/uniprot/Q8Y5K1.fasta'
outfile = ""
for line in lines:
    print(line)
    uniprotID = str(line[32:])


    print(uniprotID)
    page = requests.get(line)
    soup = BeautifulSoup(page.content, 'html.parser')
    seq = str(soup)
    blank = ''
    change = seq[:4].replace("&gt;", ">")  # first 4 char has to be replaced with > symbol
    text = change + seq[4:]

    outfile = open(uniprotID,"w")
    outfile.write(text)
    outfile.close()



'''
seq = str(soup)
blank = ''
change = seq[:4].replace("&gt;",">")# first 4 char has to be replaced with > symbol
text =change+seq[4:]

print(text)
outfile =open("FirstUniprot_Download.txt","w",)
outfile.write(text)
outfile.close()

'''

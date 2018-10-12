import urllib
import urllib.request
from bs4 import BeautifulSoup
import os

def make_soup(url):
    thepage = urllib.request.urlopen(url)
    soupdata =BeautifulSoup(thepage,"html.parser")
    return soupdata


playerdatasaved =""
playername = ""
soup = make_soup("http://www.basketball-reference.com/players/a/")

for record in soup.findAll('tr'):#This loop to print all the rows in the table
    playerdata= ""
    for names in record.findAll('th'):
        playername = playername +","+names.text
        for data in record.findAll('td'):#This loop is to print all the data in each record
            playerdata = playerdata+","+ data.text
    if len(playerdata)!=0:
        playerdatasaved = playerdatasaved + "\n" + playername[1:]+playerdata[1:]

'''
header = "Player,From,To,Pos,Wt,Birth Date,College"
file = open(os.path.expanduser("Basketball.csv"),"wb")
file.write(bytes(header,encoding="ascii",errors='ignore'))
file.write(bytes(playerdatasaved,encoding="ascii",errors='ignore'))
'''
print(playerdatasaved)
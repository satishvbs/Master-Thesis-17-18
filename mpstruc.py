import urllib
import urllib.request
from bs4 import BeautifulSoup


theurl = "http://blanco.biomol.uci.edu/mpstruc/#id_TRANSMEMBRANE_PROTEINS_ALPHAHELICAL:Channels_Mechanosensitive"
thepage = urllib.request.urlopen(theurl)
soup = BeautifulSoup(thepage,"html.parser")
#print('1:'+soup.find('tr',id="sf_117").text.strip()) #Channels: Mechanosensitive


for item in soup:
    pdb_id = soup.findAll('dev',class_="pdbPage")
    pdb_link = soup.findAll('dev',class_="pdbPage")
    print(pdb_id[item])
    print(": ")
    print(pdb_link[item])
    print("\n")

#print(soup.prettify())



'''
print('1:'+soup.find('tr',id="sf_117").text.strip()) #Channels: Mechanosensitive
print('2:'+soup.find('tr',id="sf_28").text.strip())  #Channels: Potassium, Sodium, & Proton Ion-Selective
print('3:'+soup.find('tr',id="sf_86").text.strip())  #Channels: Calcium Ion-Selective
print('4:'+soup.find('tr',id="sf_91").text.strip())  #Channels: Transient Receptor Potential
print('5:'+soup.find('tr',id="sf_29").text.strip())  #Channels: Other Ion Channels
print('6:'+soup.find('tr',id="sf_116").text.strip())     #Channels: Fluc Family
print('7:'+soup.find('tr',id="sf_31").text.strip())  #Channels: Aquaporins and Glyceroporins
print('8:'+soup.find('tr',id="sf_32").text.strip())  #Channels : Formate/Nitrite Transporter (FNT) Family
print('9:'+soup.find('tr',id="sf_33").text.strip())  #Channels: Urea Transporters
print('10:'+soup.find('tr',id="sf_34").text.strip())  #Channels: Gap Junctions
print('11:'+soup.find('tr',id="sf_80").text.strip())  #Channels: Intercellular
print('12:'+soup.find('tr',id="sf_35").text.strip())  #Channels: Amt/Mep/Rh proteins



'''
'''

for section in sections:
    description = sections.find(class_='desc').get_text().replace('\n', '')
    #  to avoid the new line we add-> .replace('\n','')
    print(description)
    #link = post.find('a')['href']
    #date = post.select('.post-date')[0].get_text()
    #  print(title,link,date)
    #print(inspect)

links =soup.find_all('a',href=True)
for link in links:
    if link['href'] is "#":
        continue
    #print(link['href'][0:4])
    print(link['href'])

#Web scraping in python finding all links
res= requests.get('http://blanco.biomol.uci.edu/mpstruc/#id_TRANSMEMBRANE_PROTEINS_ALPHAHELICAL:Channels_Mechanosensitive')
soup =bs4.BeautifulSoup(res.content,'lxml') #soup object to store all content
links =soup.find_all('a',href=True)
for link in links:
    if link['href'] is "#":
        continue
    #print(link['href'][0:4])
    print(link['href'])


#print(type(soup))
#print(soup)
#hi= soup.select('title') #hi -object to select anything form the page eg.we want title
#print(hi)
#b=hi[2].getText()
#print(b)

session = requests.session()

req = session.get('http://stackoverflow.com/questions/10807081/script-to-extract-data-from-wbpage')

doc = bs4.BeautifulSoup(req.content,"lxml")

'''

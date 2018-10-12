#Web scraping in python finding all links


'''
Some web links starts '#', some statrs with './' and rest proper link
task
Print all the links
1.if link starts with #, skip it
2.if link starts with ./ then replace ./ with 'https://' and print rest of the things

'''
import bs4
import requests

req_obj =requests.get('https://learncodeonline.in')
soup = bs4.BeautifulSoup(req_obj.content,'lxml')
links =soup.find_all('a',href=True)
print(links)
new_link=""
b= "https://"
#print(links)
for link in links:
    if link['href'] is "#":
        pass
    if link['href'].startswith('./'):
        temp_link = link['href']
        new_link = b+temp_link[2:]
        link['href'] = new_link
    print(link['href'])




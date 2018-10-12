'''
import requests
from bs4 import BeautifulSoup
from csv import writer

response = requests.get('http://codedemos.com/sampleblog/')

soup = BeautifulSoup(response.text, 'html.parser')

posts = soup.find_all(class_='post-preview')

with open('posts.csv', 'w') as csv_file:
    csv_writer = writer(csv_file)
    headers = ['Title', 'Link', 'Date']
    csv_writer.writerow(headers)

    for post in posts:
        title = post.find(class_='post-title').get_text().replace('\n', '')
        link = post.find('a')['href']
        date = post.select('.post-date')[0].get_text()
        csv_writer.writerow([title, link, date])



'''



import requests
from bs4 import BeautifulSoup
from csv import writer


response = requests.get('http://codedemos.com/sampleblog/')

soup = BeautifulSoup(response.text,'html.parser')

# Insect the web page to explore the structure of the web content
posts= soup.find_all(class_='post-preview')

with open('posts.csv', 'w') as csv_file:
    csv_writer= writer(csv_file,)
    #  create header for csv file
    headers = ['Title', 'Link', 'Date']
    csv_writer.writerow(headers)

    for post in posts:
        title = post.find(class_='post-title').get_text().replace('\n', '')
        #  to avoid the new line we add-> .replace('\n','')
        #  print(title)
        link = post.find('a')['href']
        date = post.select('.post-date')[0].get_text()
        #  print(title,link,date)
        csv_writer.writerow([title,link,date])


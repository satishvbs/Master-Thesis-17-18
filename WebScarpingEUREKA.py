from bs4 import BeautifulSoup as soup
import requests

my_url = 'https://www.flipkart.com/search?q=iphone&otracker=start&as-show=on&as=off'

uClient = requests.get(my_url)


page_soup = soup(uClient.content,"html.parser")


containers = page_soup.findAll("div",{"class":"col col-7-12"})
#print total number of products on the web page
print(len(containers))

print(soup.prettify(containers))

container = containers[0]
print(container.div.div["class"])


'''
filename = "ChannelsWebScrapping.csv"
f = open(filename,"w")

headers = "Description,PDB ID, Link\n"
f.write(headers)


for containers in containers:
    section_name = container.div.img["alt"]

    description = dec.findall("div", {"class":"colsomehting"})
    price =price_container[0].text.strip()

    rating_container = containers.findall()
    rating= rating_container[0].text

    print("product_name:"+ product_name)
    print("price:" + price)
    print("ratings:"+ rating)
    #string parsing

    trim_price = ''.join((price.split(',')))
    rm_rupee = trim_price.split("₹")
    add_rs_price = "Rs." +rm_rupee[1]
    split_price = add_rs_price.split('E')
    final_price = split_price[0]

    split_rating =rating.split(" ")
    final_rating = split_rating[0]

    print(product_name.replace(",","|")+","+ final_price + "," + final_rating + "\n")
    f.write(product_name.replace(",","|")+","+ final_price + "," + final_rating + "\n")
f.close()

'''
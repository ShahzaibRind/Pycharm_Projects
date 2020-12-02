from bs4 import  BeautifulSoup as soup
from urllib.request import  urlopen as uReq

my_url = "https://www.flipkart.com/search?q=Iphones&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"

uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

page_soup = soup(page_html, "html.parser")

Containers = page_soup.findAll("div", {"class": "_1HmYoV hCUpcT"})

#print(len(Containers))

#print(soup.prettify(Containers[0]))
#
Containers=Containers[0]
#print(Containers.div.img["alt"])
#
price=Containers.findAll("div", {"class":"_2mPS7z"})
print(price[0].text)
#
# # ratings=Containers.findAll("div",{"class":""})
# # print(ratings[0].text)
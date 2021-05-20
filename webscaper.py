import bs4
from urllib.request import urlopen
from bs4 import BeautifulSoup

url = 'https://www.amazon.com/s?k=wifi+adapter&crid=10AQ4LY9MRTSH&sprefix=wifi+adapt%2Caps%2C189&ref=nb_sb_ss_ts-doa-p_1_10'
urlClient = urlopen(url)

pageSoup = BeautifulSoup(urlClient.read(), "html.parser")
urlClient.close()


buffer =  pageSoup.findAll("div", {"class": "item-container"})
outFile = "WifiAdapters.csv"
headers = "brand, product, shipping \n"


file = open(outFile, "w")
file.write(headers);

for container in buffer:
    makeSP = container.div.select("a")
    brand = make_rating_sp[0].img["title"].title()
    product_name = container.div.select("a")[2].text
    shipping = container.findAll("li", {"class": "price-ship"})[0].text.strip().replace("$", "").replace(" Shipping", "")

    print("brand: " + brand + "\n")
    print("product: " + product_name + "\n")
    print("shipping: " + shipping + "\n")

    file.write(brand + ", " + product_name.replace(",", "|") + ", " + shipping + "\n")

file.close()


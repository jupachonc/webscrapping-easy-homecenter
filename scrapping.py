import requests
from bs4 import BeautifulSoup as bs

def homecenter(url):
    r = requests.get(url)
    soup = bs(r.text, "lxml")
    name = soup.find("h1", class_="jsx-2976215987 product-title").text
    brand = soup.find("div", class_="jsx-2976215987 product-brand").text
    price = int(float(soup.find("span", class_="jsx-3655512908").text[1:]) * 1000)
    return {
        "name": name + " " + brand,
        "price": price
    }

def easy(url):
    r = requests.get(url)
    soup = bs(r.text, "lxml")
    name = soup.find("h1", class_="nombre-prod-detalle").text
    price = int(float(soup.find(id="itempropprice").text.replace("\n", "").replace(",", ".")[1:]) * 1000)

    return {"name": name, "price": price}

def ironmart(url):
    r = requests.get(url)
    soup = bs(r.text, "lxml")
    name = soup.find("h1", class_="product-single__title").text
    price = int(float(soup.find("span", id="ProductPrice-product-template").text.replace("\n", "").replace(" ", "")[1:][:-3]) * 1000)
    return {"name": name, "price": price}

import requests
from bs4 import BeautifulSoup as bs
from fastapi import HTTPException, status

def homecenter(url):
    try:
        r = requests.get(url)
        soup = bs(r.text, "lxml")
        name = soup.find("h1", class_="product-title").text
        brand = soup.find("div", class_="product-brand").text
        raw_price = soup.find("div", class_="pdp-price").find("div").find_all("span")[1]
        price = int(raw_price.text.replace(".", ""))
        return {
            "name": name + " " + brand,
            "price": price
        }
    except:
        raise HTTPException(
            status_code = 410,
            detail = "Site cannnot be scrapped",
        )
    

def easy(url):
    try:
        r = requests.get(url)
        soup = bs(r.text, "lxml")
        name = soup.find("h1", class_="nombre-prod-detalle").text
        brand = soup.find("div", class_="logo-marca").text.strip()
        price = int(float(soup.find(id="itempropprice").text.replace("\n", "").replace(",", ".")[1:]) * 1000)
        return {
            "name": name + " " + brand,
            "price": price
        }
    except:
        raise HTTPException(
            status_code = 410,
            detail = "Site cannnot be scrapped",
        )

def ironmart(url):
    r = requests.get(url)
    soup = bs(r.text, "lxml")
    name = soup.find("h1", class_="product-single__title").text
    price = int(float(soup.find("span", id="ProductPrice-product-template").text.replace("\n", "").replace(" ", "")[1:][:-3]) * 1000)
    return {"name": name, "price": price}

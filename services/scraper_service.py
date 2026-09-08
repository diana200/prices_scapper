import string
import requests
from bs4 import BeautifulSoup
from config import API_KEY
import time

API_URL = "https://api.pricesapi.io/api/v1/products/search"


def scrape(url: string):
    html = requests.get(url).text
    soup = BeautifulSoup(html, "html.parser")

    print(f"==> scraped soup: {soup}")

    # Dummy selectors — replace with real ones
    name = soup.find("h1").text.strip()
    store = "eMAG" if "emag" in url else "Unknown"
    price = float(soup.find(class_="price").text.replace("lei", "").strip())
    available = "In stock" in html

    return {
        "name": name,
        "store": store,
        "price": price,
        "available": available,
        "url": url
    }


def scrape_products(productName: string = "iphone", country: string = 'ro', number_offers: int = 5):
    """
        supports only 6 requests per minute
    :param productName:
    :param country:
    :param number_offers:
    :return:
    """
    response_data = {
        "products":[]
    }

    if len(productName)>1:

        params = {
            "q":productName,
            "country":country,
            "limit":number_offers
        }

        headers = {
            "x-api-key":API_KEY
        }

        # supports only 6 requests per minute
        response = requests.get(
            url=API_URL,
            params=params,
            headers=headers
        )

        if response.status_code == 200:
            data = response.json()

            if data["data"] and data["data"]["products"]:
                print("nr products: ", len(data["data"]["products"]))
                response_data = {
                    "products": data["data"]["products"]
                }
        # elif response.status_code == 503:
        #     retry_after = int(response.headers.get("Retry-After", 5))
        #     time.sleep(retry_after)
        else:
            print("ScrapeService - Error while requesting products!\n Http status code: ", response.status_code)

    return response_data

def request_data(url, params, headers):
    response_data = {
        "products": []
    }

    response = requests.get(
        url=API_URL,
        params=params,
        headers=headers
    )

    if response.status_code == 200:
        data = response.json()

        if data["data"] and data["data"]["products"]:
            print("nr products: ", len(data["data"]["products"]))
            response_data = {
                "products": data["data"]["products"]
            }
        # If service unavailable or rate-limited
    elif response.status_code in (429, 503):
        retry_after = response.headers.get("Retry-After")

        if retry_after:
            wait_time = int(retry_after)
            print(f"Server asked us to wait {wait_time} seconds...")
            time.sleep(wait_time)
        else:
            # fallback if header missing
            print("Retry-After missing, waiting 5 seconds...")
            time.sleep(5)

        # retry once after waiting
        request_data(url, params, headers)
    else:
        print("ScrapeService - Error while requesting products!\n Http status code: ", response.status_code)
        print(response.__dict__)

    return response_data


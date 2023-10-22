import http.client

from config import xrapidapi_key


def get_product_inf_by_barcode(barcode):
    conn = http.client.HTTPSConnection("barcode-lookup.p.rapidapi.com")

    headers = {
        'X-RapidAPI-Key': xrapidapi_key,
        'X-RapidAPI-Host': "barcode-lookup.p.rapidapi.com"
    }

    conn.request("GET", f"/v3/products?barcode={barcode}", headers=headers)

    res = conn.getresponse()
    data = res.read()

    return data.decode("utf-8")
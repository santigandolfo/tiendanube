from fastapi import FastAPI
import requests
from ShippingOptions import ShippingOptions

testExternalAPI = "https://shipping-options-api.herokuapp.com/v1/shipping_options"

app = FastAPI()


@app.get("/shippingOptions")
def shippingOptions():
    r = requests.get(testExternalAPI)
    if (r.status_code == 200):
        print(r.json()["shipping_options"])
        shippingOptions= ShippingOptions(r.json()["shipping_options"])
        return shippingOptions.getSortedOptions()
    return r



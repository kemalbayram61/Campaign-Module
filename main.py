from fastapi import FastAPI
from pydantic import BaseModel
from Data.ProductHelper import ProductHelper
from Object.Basket import Basket
from Object.Product import Product

class RequestProduct(BaseModel):
    id:str
    qty: int

class Request(BaseModel):
    id: str
    customerID: str
    productList: list[RequestProduct]
    paymentTypeID: str
    paymentChannelID: str

app = FastAPI()

def get_basked(request: Request)->Basket:
    productList: list[Product] = []
    for product in request.productList:
        product_helper = ProductHelper(product.id)
        product = product_helper.get()
        if(product is not None):
            productList.append(product)

    basket: Basket = Basket(customerID=request.customerID,
                            paymentChannelID=request.paymentChannelID,
                            paymentTypeID=request.paymentTypeID,
                            productList=productList)

    return basket

@app.post("/find_campaign_list")
def find_campaign_list(request: Request):
    basket: Basket = get_basked(request)
    return basket
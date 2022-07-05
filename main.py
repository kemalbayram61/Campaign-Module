from fastapi import FastAPI
from Object.Basket import Basket

app = FastAPI()

@app.post("/find_campaign_list")
def find_campaign_list(basket: Basket):
    return {basket.id:basket.customerID}
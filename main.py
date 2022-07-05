from fastapi import FastAPI
from Object.Basket import Basket

app = FastAPI()

@app.post("/find_campaign_list")
def find_campaign_list(request: Basket):
    return {request.id:request.customerID}
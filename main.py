from fastapi import FastAPI
from pydantic import BaseModel

class Request(BaseModel):
    id: str
    customerID: str
    productList: list[str]
    paymentTypeID: str
    paymentChannelID: str

app = FastAPI()

@app.post("/find_campaign_list")
def find_campaign_list(request: Request):
    return {request.id:request.customerID}
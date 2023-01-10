from typing import Union

from fastapi import FastAPI, HTTPException, status

from pydantic import BaseModel

from scrapping import *

app = FastAPI()

class Query(BaseModel):
    site: str
    url: str
    
    
    
@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/query")
def read_price(query: Query):
    site = query.site
    if site == "ES":
        return easy(query.url)
    elif site == "HC":
        return homecenter(query.url)
    else:
        raise HTTPException(
            status_code = 400,
            detail = "Site not supported",
        )
    

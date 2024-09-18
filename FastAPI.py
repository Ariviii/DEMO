from fastapi import FastAPI # type: ignore
from pydantic import BaseModel

import uvicorn
app = FastAPI()

class Filename(BaseModel):
    Data:str
    Status: list




@app.get("/get_api")
def Sense():
    return "get Application Interface"


@app.post("/sensor_data")
def receive_sensor_data(data:Filename):
    print("\n[<---]Reciving Data: ",type(data),"\n")
    print("\n[Live Data]: ",data)
    return "200"




if __name__ == "__main__":
   # uvicorn.run('FastAPI:app', host='localhost', port=9004, workers=2)    
     uvicorn.run('main:app', host='0.0.0.0', port=9004, workers=2)

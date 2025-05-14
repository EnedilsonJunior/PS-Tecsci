from fastapi import FastAPI
import uvicorn
from database import Inversor_DB, Usinas_DB


app = FastAPI()

@app.get("/inversor")
def read_inversor():
    return Inversor_DB
@app.get("/usina")
def read_usina(): 
    return Usinas_DB 
 
if __name__ == "__main__":
    uvicorn.run(app, port=8000)
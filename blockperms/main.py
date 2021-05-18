from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel
from functions import permission
from functions import blockchain
from functions import account


#to see api documentation go to your-link/docs or your-link/redoc

class Permission(BaseModel):
    sender: str
    receiver: str
    permission: Optional[bool] = None
    #type: # Optional[tuple] = None

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Api is running"}

@app.get("/permissions/check")
async def check_permission():
    return {"permission": permission.check_permission("0x490CD3cAbED9f706055e617Ed09F96a905E0BD31", "0x50b72d23E5F3c1E0002E2E4C44C2f01ddd605b6F")}

@app.get("/permissions/set")
async def set_permissions():
    sender = '0x490CD3cAbED9f706055e617Ed09F96a905E0BD31'
    sender_pass = 'root'
    they = '0x50b72d23E5F3c1E0002E2E4C44C2f01ddd605b6F'
    they_pass = 'root'
    return {"Permission": permission.set_permission(sender, sender_pass, they, they_pass)}

@app.get("/test")
async def connection_check():
    return {blockchain.connection_setup()}

@app.get("/accounts")
async def get_accounts():
    return {"Accounts": account.list_accounts()}


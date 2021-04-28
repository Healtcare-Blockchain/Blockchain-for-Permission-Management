from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel
from functions import permission


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
    return {"permission": permission.check_permission("0xD3bb2A7a09a7b9DDa8D55Be15f5e3f9092BE8A37", "0xe3AB610EB45ca7Af9d529C46812e550B62c4Ff5c")}

@app.get("/permissions/set")
async def set_permissions():
    sender = '0xD3bb2A7a09a7b9DDa8D55Be15f5e3f9092BE8A37'
    sender_pass = 'Chasity-Lent-Dab-Gigahertz-Litter3-Drastic'
    they = '0xe3AB610EB45ca7Af9d529C46812e550B62c4Ff5c'
    they_pass = 'a2f44c8fb33b804616dc2d9ae1420158c415ae2883078830773a658017d2d746'
    return {"Permission": permission.set_permission(sender, sender_pass, they, sender_pass)}

@app.get("/permission/check")
async def permission_check():
    return {"permission": "True"}

@app.get("/permission/set")
async def permission_set():
    return {"Permission": "Set True between 0xD3bb2A7a09a7b9DDa8D55Be15f5e3f9092BE8A37 : 0xe3AB610EB45ca7Af9d529C46812e550B62c4Ff5c"}


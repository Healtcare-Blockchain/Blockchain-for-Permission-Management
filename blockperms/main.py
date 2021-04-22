from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel
from blockperms.functions import permission


#to see api documentation go to your-link/docs or your-link/redoc

class Permission(BaseModel):
    sender: str
    receiver: str
    permission: Optional[bool] = None
    #type: #Optional[tuple] = None

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Api is running"}

@app.get("/permissions/check")
async def checkPermission():
    return {"permission": permission.check_permission("0xD3bb2A7a09a7b9DDa8D55Be15f5e3f9092BE8A37", "0xe3AB610EB45ca7Af9d529C46812e550B62c4Ff5c")}

@app.get("/permissions/set")
async def setPermissions():
    return {"Permission": permission.set_permission("0xD3bb2A7a09a7b9DDa8D55Be15f5e3f9092BE8A37", "0xe3AB610EB45ca7Af9d529C46812e550B62c4Ff5c")}
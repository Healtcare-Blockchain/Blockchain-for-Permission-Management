from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel


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
async def checkPermission(permission: Permission):
    return {"permission": "granted"}

@app.get("/permissions/set")
async def setPermissions():
    return {"Permission": "Permission has been set or updated"}
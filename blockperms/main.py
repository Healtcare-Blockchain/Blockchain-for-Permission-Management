from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel
from functions import permission
from functions import blockchain
from functions import account
import xml.etree.ElementTree as ET


#to see api documentation go to your-link/docs or your-link/redoc

class Permission(BaseModel):
    SenderId: str
    ReceiverId: str
    Permission: Optional[bool] = None
    #type: # Optional[tuple] = None

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Api is running"}

@app.post("/permissions/check")
async def check_permission(permission : Permission):
    verry_secure_file = ET.parse('users.xml')
    root = verry_secure_file.getroot()
    # users = verry_secure_file.getElementByTagName('user')
    sender = None
    receiver = None

    for user in root:
        print(user[1].attrib)
        print(permission.SenderId)
        if user[0].attrib == permission.SenderId:
            sender = user[1].attrib
        elif user[0].attrib == permission.SenderId:
            receiver = user[1].attrib

    if sender or receiver == None:
        print(sender + receiver)
        return {"Error": "One or more users dont exist"}

    return {"permission": permission.check_permission(sender, receiver)}

@app.post("/permissions/set")
async def set_permissions(permission : Permission):
    verry_secure_file = ET.parse('users.xml')
    root = verry_secure_file.getroot()
    # users = verry_secure_file.getElementByTagName('user')
    sender = None
    receiver = None

    for user in root:
        if user[0] == permission.SenderId:
            sender = user[1]
            sender_pass = user[2]
        elif user[0] == permission.SenderId:
            receiver = user[1]
            receiver_pass = user[2]

    if sender or receiver == None:
        print(sender + receiver)
        return {"Error": "One or more users dont exist"}

    return {"Permission": permission.set_permission(sender, sender_pass, receiver, receiver_pass, permission.permission)}

@app.get("/test")
async def connection_check():
    return {blockchain.connection_setup()}

@app.get("/accounts")
async def get_accounts():
    return {"Accounts": account.list_accounts()}


from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
from functions import blockchain
from functions import account
from functions import permission as perm
import xml.etree.ElementTree as ET

# to see api documentation go to your-link/docs or your-link/redoc

class Permission(BaseModel):
    SenderId: str
    ReceiverId: str
    Permission: Optional[bool] = None
    #type: # Optional[tuple] = None

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Api is running!!!"}


@app.post("/permissions/check")
async def check_permission(permission : Permission):
    verry_secure_file = ET.parse('users.xml')
    root = verry_secure_file.getroot()
    sender = "empty"
    receiver = "empty"

    for user in root:
        print(user[1].text)
        print(permission.SenderId)
        if user[0].text == permission.SenderId:
            sender = user[1].text
        elif user[0].text == permission.ReceiverId:
            receiver = user[1].text

    # if sender or receiver == None:
    #     print(sender +" "+ receiver)
    #     return {"Error": "One or more users dont exist"}

    return {"permission": perm.check_permission(sender, receiver)}

@app.post("/permissions/set")
async def set_permissions(permission : Permission):
    verry_secure_file = ET.parse('users.xml')
    root = verry_secure_file.getroot()
    # users = verry_secure_file.getElementByTagName('user')
    sender = "Empty"
    receiver = "Empty"
    sender_pass = "Empty"
    receiver_pass = "Empty"

    for user in root:
        if user[0].text == permission.SenderId:
            sender = user[1].text
            sender_pass = user[2].text
        elif user[0].text == permission.ReceiverId:
            receiver = user[1].text
            receiver_pass = user[2].text

    # if sender or receiver == None:
    #     print(sender + receiver)
    #     return {"Error": "One or more users dont exist"}

    return {"Permission": perm.set_permission(sender, sender_pass, receiver, receiver_pass, permission.Permission)}

@app.get("/test")
async def connection_check():
    return {blockchain.connection_setup()}

@app.get("/accounts")
async def get_accounts():
    return {"Accounts": account.list_accounts()}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
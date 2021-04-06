from fastapi import FastAPI

import permission_functions as pmf

#to see api documentation go to http://127.0.0.1:8000/docs or http://127.0.0.1:8000/redoc


app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Api is running"}


@app.post("/post/permissions/")
async def set_permission(sender: str, they: str):
    return {pmf.set_permission(sender, they)}

@app.get("/get/permissions/")
async def check_permission(sender: str, they: str):
    return {pmf.check_permission()}
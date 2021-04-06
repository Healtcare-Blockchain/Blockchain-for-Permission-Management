from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Api is running"}


@app.post("/post/permissions/")
async def set_Permission(sender: str, they: str):
    return {"message": "Api is running"}

@app.get("/get/permissions/")
async def set_Permission(sender: str, they: str):
    return {"message": "Api is running"}
from fastapi import FastAPI

#to see api documentation go to your-link/docs or your-link/redoc


app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Api is running"}


@app.post("/post/permissions/")
async def set_permission():
    sender = ""
    they = ""
    return {'true'}

@app.get("/get/permissions/")
async def check_permission():
     return {'done'}
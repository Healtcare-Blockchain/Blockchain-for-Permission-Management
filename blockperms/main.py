from fastapi import FastAPI

#to see api documentation go to your-link/docs or your-link/redoc


app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Api is running"}
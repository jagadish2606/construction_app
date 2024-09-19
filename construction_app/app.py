from fastapi import FastAPI
from construction_app.endpoints import user

app = FastAPI()

# Include your endpoints
app.include_router(user.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to Adhi Construction API"}

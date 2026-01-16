import uvicorn
from fastapi import FastAPI
from src.web import user, creature, auth

app = FastAPI()
app.include_router(user.router)
app.include_router(creature.router)
app.include_router(auth.router)

@app.get("/")
def top():
    return "top here"

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True, host="0.0.0.0", port=8000)
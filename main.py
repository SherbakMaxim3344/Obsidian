import uvicorn
from fastapi import FastAPI
from src.web import explorer, creature

app = FastAPI()
app.include_router(explorer.router)
app.include_router(creature.router)

@app.get("/")
def top():
    return "top here"

@app.get("/echo/{thing}")
def echo(thing):
    return f"echoing {thing}"

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True, host="0.0.0.0", port=8000)
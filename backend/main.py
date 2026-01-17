from multiprocessing import allow_connection_pickling
import uvicorn
from fastapi import FastAPI
from src.web import user, auth
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3001"],  # Откуда разрешаем запросы
    allow_credentials=True,
    allow_methods=["*"],  # Разрешаем все HTTP-методы
    allow_headers=["*"],  # Разрешаем все заголовки
)

app.include_router(user.router)
app.include_router(auth.router)

@app.get("/")
def top():
    return "top here"

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True, host="0.0.0.0", port=8000)
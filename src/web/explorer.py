from fastapi import APIRouter, status
from src.model.explorer import Explorer
import src.service.explorer as service

router = APIRouter(prefix= "/explorer")

@router.get("") #/explorer
@router.get("/", status_code=200) #/explorer/
def get_all() -> list[Explorer]:
    return service.get_all()

@router.get("/{name}")
def get_one(name: str) -> Explorer | None:
    return service.get_one(name)

@router.post("/", status_code=201)
def create(explorer: Explorer) -> Explorer:
    return service.create(explorer)

@router.put("/")
def replace(explorer: Explorer) -> Explorer:
    return service.modify(explorer)

@router.delete("/{name}", status_code=204)
def delete(name: str):
    service.delete(name)
    return None
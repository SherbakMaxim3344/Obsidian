from src.model.explorer import Explorer
import src.data.explorer as data

def get_all() -> list[Explorer]:
    return data.get_all()

def get_one(name: str) -> Explorer | None:
    return data.get_one(name)

def create(explorer: Explorer) -> Explorer:
    return data.create(explorer)

def replace(id, explorer: Explorer) -> Explorer:
    return data.replace(id, explorer)

def modify(explorer: Explorer) -> Explorer:
    return data.modify(explorer)

def delete(name: str) -> bool:  
    return data.delete(name)
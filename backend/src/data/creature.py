from .init import conn, curs
from src.model.creature  import Creature

curs.execute("""create table if not exists creature(
                name text primary key,
                description text,
                country text,
                area text,
                aka text
    )""")
conn.commit()

# преобразует кортеж, возвращаемый функцией fetch, в объект модели
def row_to_model(row: tuple) -> Creature:
    name, description, country, area, aka = row
    return Creature(name, description, country, area, aka)

# переводит Pydantic-модель в словарь, пригодный для использования в качестве именованного параметра запроса
def model_to_dict(creature: Creature) -> dict:
    return creature.model_dump()
def get_one(name: str) -> Creature:
    qry = "select * from creature where name=:name"
    params = {"name": name}
    curs.execute(qry, params)
    return row_to_model(curs.fetchone())

def get_all(name: str) -> list[Creature]:
    qry = "select * from creature"
    curs.execute(qry)
    return [row_to_model(row) for row in curs.fetchall()]

def create(creature: Creature):
    qry = """ insert into creature values
        (:name, :description, :country, :area, :aka)
    """
    params = model_to_dict(creature)
    curs.execute(qry, params)
    conn.commit()
    return get_one(creature.name)
    
def modify(creature: Creature) -> Creature:
    qry = """update creature
            set country=:country,
                name=:name,
                description=:description,
                area=:area,
                aka=:aka
            where name=:name_origin
        """
    params = model_to_dict(creature)
    params["name_origin"]=creature.name
    _ = curs.execute(qry, params)
    conn.commit()
    return get_one(creature.name)

def replace(creature: Creature):
    return creature

def delete(name: str) -> bool:
    qry= "delete from creature where name = :name"
    params = {"name": name}
    res = curs.execute(qry, params)
    conn.commit()
    return bool(res)
from src.model.user import UserInDB, UserPublic
from datetime import datetime
from .init import get_cursor, get_connection

conn = get_connection()
curs = get_cursor()

curs.execute("""create table if not exists users(
    id integer primary key autoincrement,
    username text unique not null,
    email text unique not null,
    password_hash text not null,
    avatar_url text,
    bio text,
    created_at timestamp not null,
    updated_at timestamp,
    last_login timestamp,
    is_active boolean default true,
    is_verified boolean default false
)""")
conn.commit()

def row_to_model(row: tuple) -> UserInDB:
    return UserInDB(
        id=row[0],
        username=row[1],
        email=row[2],
        password_hash=row[3],
        avatar_url=row[4],
        bio=row[5],
        created_at=datetime.fromisoformat(row[6]) if row[6] else None,
        updated_at=datetime.fromisoformat(row[7]) if row[7] else None,
        last_login=datetime.fromisoformat(row[8]) if row[8] else None,
        is_active=bool(row[9]),
        is_verified=bool(row[10])
    )

def model_to_dict(user: UserInDB) -> dict:
    return user.model_dump()

def get_one(username:str) ->UserInDB | None:
    qry="select * from users where username=:username"
    params = {"username": username} #Это словарь для безопасной подстановки
    curs.execute(qry, params)
    row = curs.fetchone()
    return row_to_model(row) if row else None#возвращает кортеж если нашел

def get_all() -> list[UserInDB]:
    qry="select * from users"
    curs.execute(qry)
    return [row_to_model(row) for row in curs.fetchall()]

def create(user: UserInDB) -> UserInDB:
    qry = """insert into users 
        (username, email, password_hash, avatar_url, bio, 
        created_at, updated_at, last_login, is_active, is_verified)
        values (:username, :email, :password_hash, :avatar_url, :bio,
        :created_at, :updated_at, :last_login, :is_active, :is_verified)"""
    params = model_to_dict(user)
    curs.execute(qry, params)
    conn.commit()
    # Получаем ID
    user.id = curs.lastrowid
    return user

def replace(old_username: str, user: UserInDB) -> UserInDB:
    qry = """update users set
            username=:username, email=:email, password_hash=:password_hash,
            avatar_url=:avatar_url, bio=:bio, updated_at=:updated_at,
            last_login=:last_login, is_active=:is_active, is_verified=:is_verified
            where username=:old_username"""
    
    params = model_to_dict(user)
    params["old_username"] = old_username
    
    curs.execute(qry, params)
    conn.commit()
    
    updated_user = get_one(user.username)
    if not updated_user:
        raise ValueError(f"User {user.username} not found after update")
    return updated_user

def delete(username: str) -> bool:
    qry = "delete from users where username = :username"
    curs.execute(qry, {"username": username})
    conn.commit()
    return curs.rowcount > 0  
import os
from pathlib import Path
from sqlite3 import connect, Connection, Cursor, IntegrityError

conn: Connection | None=None
curs: Cursor | None=None

def get_db(name: str | None=None, reset: bool=False):
    # *Подключение к файлу БД
    global conn, curs
    if conn:
        if not reset:
            return
        conn = None
    if not name:
        name = os.getenv("CRYPTID_SQLITE_DB") # Пробуем взять из переменной окружения
            # 1. Находим корневую директорию проекта
            # __file__ = путь к текущему файлу (например, /home/.../src/data/creature.py)
            # .resolve() = преобразует в абсолютный путь
            # .parents[1] = поднимаемся на 2 уровня вверх
        top_dir = Path(__file__).resolve().parents[1]
        db_dir = top_dir / "db"
        db_dir.mkdir(exist_ok=True, mode=0o755)  # ← создаём папку если нет
        db_name = "cryptid.db"
        db_path = str(db_dir / db_name)
        name = os.getenv("CRYPTID_SQLITE_DB", db_path)
    conn=connect(name, check_same_thread=False)
    curs=conn.cursor()

get_db()
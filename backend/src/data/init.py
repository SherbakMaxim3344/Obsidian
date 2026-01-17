import os
from pathlib import Path
from sqlite3 import connect, Connection, Cursor, IntegrityError

conn: Connection | None = None
curs: Cursor | None = None

def get_db(name: str | None = None, reset: bool = False) -> None:
    """Initialize database connection"""
    global conn, curs
    if conn and not reset:
        return
    
    if not name:
        name = os.getenv("CRYPTID_SQLITE_DB")
        if not name:
            # 1. Находим корневую директорию проекта
            top_dir = Path(__file__).resolve().parents[1]
            db_dir = top_dir / "db"
            db_dir.mkdir(exist_ok=True, mode=0o755)
            db_name = "cryptid.db"
            db_path = str(db_dir / db_name)
            name = db_path
    
    conn = connect(name, check_same_thread=False)
    curs = conn.cursor()

def get_cursor() -> Cursor:
    """Get database cursor, ensuring connection is initialized"""
    global conn, curs
    if not conn or not curs:
        get_db()
    if not curs:
        raise RuntimeError("Database cursor is not initialized")
    return curs

def get_connection() -> Connection:
    """Get database connection, ensuring it's initialized"""
    global conn
    if not conn:
        get_db()
    if not conn:
        raise RuntimeError("Database connection is not initialized")
    return conn

# Автоматически инициализируем при импорте
get_db()
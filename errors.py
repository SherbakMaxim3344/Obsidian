class Missing(Exception):
    """Запись не найдена"""
    def __init__(self, msg: str):
        super().__init__(msg)
        self.msg = msg

class Duplicate(Exception):
    """Дубликат записи (например, пользователь с таким именем уже существует)"""
    def __init__(self, msg: str):
        super().__init__(msg)
        self.msg = msg
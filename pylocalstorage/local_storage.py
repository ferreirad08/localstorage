from threading import Lock
from json import dumps, loads

from sqlalchemy import create_engine, text

from .exceptions import WriteStorageError


class LocalStorage:

    __engine = None
    __lock = Lock()
    __version__ = "1.3.0"

    length = 0

    def __init__(self) -> None:
        dbpath = __file__.replace("pylocalstorage.py", "localStorage.db")
        self.__engine = create_engine(f"sqlite:///{dbpath}")

        self.__executeQuery("""
        CREATE TABLE IF NOT EXISTS LocalStorage (
            key TEXT UNIQUE,
            value TEXT
        );
        """)
        self.__update_length()

    def setItem(self, key, value) -> None:
        try:
            value_str = dumps(value)
            self.__executeQuery(f"""
            INSERT INTO LocalStorage (key, value)
            VALUES ('{key}','{value_str}')
            ON CONFLICT(key) DO UPDATE SET value = '{value_str}';
            """)
            self.__update_length()
        except:
            raise WriteStorageError

    def getItem(self, key):
        result = list(self.__executeQuery(f"""
        SELECT value
        FROM LocalStorage
        WHERE key = '{key}';
        """))
        if result:
            return loads(result[0][0])

    def removeItem(self, key) -> None:
        self.__executeQuery(f"""
        DELETE FROM LocalStorage
        WHERE key = '{key}';
        """)
        self.__update_length()

    def clear(self) -> None:
        self.__executeQuery("DELETE FROM LocalStorage;")
        self.__update_length()

    def key(self, index: int):
        if isinstance(index, int) and 0 <= index < self.length:
            result = self.__executeQuery("SELECT key FROM LocalStorage;")
            return list(result)[index][0]

    def __update_length(self) -> None:
        result = self.__executeQuery("SELECT COUNT(*) FROM LocalStorage;")
        self.length = list(result)[0][0]

    def __executeQuery(self, query):
        with self.__lock:
            with self.__engine.begin() as connection:
                return connection.execute(text(query))

import sqlite3
from config import DATABASE_PATH
import threading
import hashlib

class DatabaseManager:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super(DatabaseManager, cls).__new__(cls)
                    cls._instance.init()
        return cls._instance

    def init(self):
        self.local = threading.local()

    def get_connection(self):
        if not hasattr(self.local, 'connection'):
            self.local.connection = sqlite3.connect(DATABASE_PATH)
            self.create_tables(self.local.connection)
        return self.local.connection

    def create_tables(self, conn):
        cursor = conn.cursor()
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS content
        (id INTEGER PRIMARY KEY, source TEXT UNIQUE, content TEXT)
        ''')
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS users
        (id INTEGER PRIMARY KEY, username TEXT UNIQUE, password TEXT)
        ''')
        conn.commit()

    def save_content(self, source, content):
        conn = self.get_connection()
        with conn:
            conn.execute("INSERT OR REPLACE INTO content (source, content) VALUES (?, ?)", (source, content))

    def get_content(self, source):
        conn = self.get_connection()
        with conn:
            cursor = conn.execute("SELECT content FROM content WHERE source = ?", (source,))
            result = cursor.fetchone()
        return result[0] if result else None

    def register_user(self, username, password):
        conn = self.get_connection()
        try:
            hashed_password = hashlib.sha256(password.encode()).hexdigest()
            with conn:
                conn.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hashed_password))
            return True
        except sqlite3.IntegrityError:
            return False

    def verify_user(self, username, password):
        conn = self.get_connection()
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        with conn:
            cursor = conn.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, hashed_password))
            return cursor.fetchone() is not None
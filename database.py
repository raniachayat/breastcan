import sqlite3
import hashlib
import os

DB_FILE = "users.db"

# ------------------ Helper Functions ------------------
def hash_password(password):
    """Hash a password using SHA-256"""
    return hashlib.sha256(password.encode()).hexdigest()

# ------------------ Initialize Database ------------------
def init_db():
    """
    Create the users table if it doesn't exist.
    """
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS users (
            username TEXT PRIMARY KEY,
            password TEXT
        )
    ''')
    conn.commit()
    conn.close()

# ------------------ User Functions ------------------
def add_user(username, password):
    """
    Add a new user. Password is hashed before saving.
    Returns True if successful, False if username exists.
    """
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    try:
        hashed_pw = hash_password(password)
        c.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hashed_pw))
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False  # Username already exists
    finally:
        conn.close()

def authenticate_user(username, password):
    """
    Check if the username/password combination is correct.
    """
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    hashed_pw = hash_password(password)
    c.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, hashed_pw))
    user = c.fetchone()
    conn.close()
    return user is not None

def user_exists(username):
    """
    Check if a username already exists.
    """
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE username = ?", (username,))
    exists = c.fetchone() is not None
    conn.close()
    return exists

# ------------------ Initialize DB ------------------
init_db()

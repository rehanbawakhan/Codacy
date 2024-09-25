import sqlite3

# Connect to an in-memory SQLite database (no file stored on disk)
conn = sqlite3.connect(':memory:')
cursor = conn.cursor()

# Create a simple users table
cursor.execute('''CREATE TABLE users (id INTEGER PRIMARY KEY, username TEXT, password TEXT)''')

# Insert some dummy data
cursor.execute("INSERT INTO users (username, password) VALUES ('alice', 'password123')")
cursor.execute("INSERT INTO users (username, password) VALUES ('bob', 'qwerty')")

conn.commit()

# Vulnerable function to authenticate users
def login(username, password):
    # This is vulnerable to SQL injection
    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    cursor.execute(query)
    result = cursor.fetchall()

    if result:
        print(f"Welcome {username}!")
    else:
        print("Login failed.")

# Simulating normal login
print("Normal login attempt:")
login('alice', 'password123')

# SQL Injection attack
print("\nSQL Injection attack attempt:")
malicious_input = "' OR '1'='1"
login(malicious_input, 'doesnotmatter')  # Bypasses authentication

conn.close()

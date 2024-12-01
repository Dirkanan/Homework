import sqlite3

connection = sqlite3.connect("not_telegram.db")
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL
)
''')

cursor.execute("CREATE INDEX IF NOT EXISTS idx_email ON Users (email)")

for i in range(10):
    cursor.execute("INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)",
                   (f"User{i + 1}", f"example{i + 1}@gmail.com", (i + 1) * 10, 1000))

cursor.execute("UPDATE Users SET balance = balance - 500 WHERE id % 2 = 1")

cursor.execute(
    "DELETE FROM Users WHERE id IN (SELECT id FROM (SELECT id, ROW_NUMBER() OVER (ORDER BY id) AS us FROM Users) WHERE us % 3 = 1)")
# вот это пункт задания сделал BRUTALITY моему мозгу
cursor.execute("SELECT username, email, age, balance FROM Users WHERE age != 60")
results = cursor.fetchall()
for row in results:
    username, email, age, balance = row
    print(f'Имя: {username} | Почта: {email} | Возраст: {age} | Баланс: {balance}')

connection.commit()
connection.close()

import sqlite3

connection = sqlite3.connect('module14\Создание БД, добавление, выбор и удаление элементов\\not_telegram.db')

cursor = connection.cursor()

cursor.execute('''
               CREATE TABLE IF NOT EXISTS Users(
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   username TEXT UNIQUE NOT NULL,
                   email TEXT UNIQUE NOT NULL,
                   age INTEGER,
                   balance INTEGER NOT NULL)''')

cursor.execute('''
               CREATE INDEX IF NOT EXISTS index_email ON Users(email)''')

cursor.execute("DELETE FROM Users")

for i in range(1, 11):
    cursor.execute('INSERT INTO Users(username, email, age, balance) VALUES(?, ?, ?, ?)', (f'User{i}', f'example{i}@gmail.com', 10 * i, 1000))

for i in range(1, 11, 2):
    cursor.execute(f"UPDATE Users SET balance = ? WHERE username = ?", (500, f'User{i}'))

for i in range(1, 11, 3):
    cursor.execute(f'DELETE FROM Users WHERE username = ?', (f'User{i}',))
connection.commit()

cursor.execute('SELECT username, email, age, balance FROM Users WHERE age != 60')

results = cursor.fetchall()
for user in results:
    print(f"Имя: {user} | Почта: {user[1]} | Возраст: {user[2]} | Баланс: {user[3]}")


connection.close()
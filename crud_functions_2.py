import sqlite3

connection = sqlite3.connect("Products.db")
cursor = connection.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS Products(
id INTEGER PRIMARY KEY,
title TEXT NOT NULL,
description TEXT ,
price INTEGER NOT NULL
)
''')

conn = sqlite3.connect('Users.db')
cur = conn.cursor()

cur.execute('''
CREATE TABLE IF NOT EXISTS Users (
id INTEGER PRIMARY KEY AUTOINCREMENT,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER NOT NULL,
balance INTEGER NOT NULL
)
''')

conn.commit()


def add_user(username, email, age):
    check_user = cur.execute("SELECT * FROM Users WHERE username=?", (username,))
    if check_user.fetchone() is None:
        insert_query = """
        INSERT INTO Users (username, email, age, balance) 
        VALUES (?, ?, ?, ?);
        """
        cur.execute(insert_query, (username, email, age, 1000))
        conn.commit()


def is_included(username):
    select_query = "SELECT EXISTS(SELECT 1 FROM Users WHERE username=? LIMIT 1);"
    cur.execute(select_query, (username,))
    result = cur.fetchone()[0]
    return bool(result)


def add_product(quantity):
    for number in range(quantity):
        product_id = number + 1
        check_product = cursor.execute("SELECT * FROM Products where id=?", (product_id,))
        title = f"Продукт {number + 1}"
        description = f"Описание {number + 1}"
        price = (number + 1) * 100
        if check_product.fetchone() is None:
            cursor.execute(f'''
            INSERT INTO Products VALUES( '{product_id}', '{title}', '{description}', '{price}')
            ''')


connection.commit()


def get_all_products():
    connection = sqlite3.connect("Products.db")
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM Products')
    products = cursor.fetchall()
    connection.close()
    return products


get_all_products()
conn.commit()

connection.commit()


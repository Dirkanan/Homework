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
connection.commit()
connection.close()

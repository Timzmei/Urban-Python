import sqlite3
import os

def connect_db():
    return sqlite3.connect('module14\\Написание примитивной ORM\\products.db')

def initiate_db():
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute ('''
        CREATE TABLE IF NOT EXISTS Products (
            id INTEGER PRIMARY KEY,
            title TEXT NOT NULL,
            description TEXT,
            price INTEGER NOT NULL,
            filename TEXT
        )
    ''')
    cursor.execute ('''
        CREATE TABLE IF NOT EXISTS Users (
            id INTEGER PRIMARY KEY,
            username TEXT NOT NULL,
            email TEXT NOT NULL,
            age INTEGER NOT NULL,
            balance INTEGER NOT NULL
        )
    ''')
    connection.commit()
    connection.close()

def get_all_products():
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute ('''
        SELECT * FROM Products
    ''')
    products = cursor.fetchall()
    connection.close()
    return products

def add_product(title, description, price):
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute ('''
        INSERT INTO Products (title, description, price, filename)
        VALUES (?, ?, ?, ?)
    ''', (title, description, price))
    connection.commit()
    connection.close()
    

def add_user(username, email, age):
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute ('''
        INSERT INTO Users (username, email, age, balance)
        VALUES (?, ?, ?, ?)
    ''', (username, email, age, 1000))
    connection.commit()
    connection.close()


initiate_db()

def populate_products():
    products = [
        ('Помидоры', 'Свежие помидоры', 100, 'tomato'),
        ('Баклажаны', 'Свежие баклажаны', 120, 'eggplant'),
        ('Лук', 'Свежий лук', 80, 'onion'),
        ('Картофель', 'Свежий картофель', 90, 'potato')
    ]
    connection = connect_db()
    cursor = connection.cursor()
    cursor.executemany ('''
        INSERT INTO Products (title, description, price, filename)
        VALUES (?, ?, ?, ?)
    ''', products)
    connection.commit()
    connection.close()

populate_products()

def is_included(username):
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute ('''
        SELECT * FROM Users 
        WHERE username = ?
    ''', (username,))
    user = cursor.fetchone()
    connection.close()
    if user is not None:
        return True
    else:
        return False

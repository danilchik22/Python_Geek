import mysql.connector
from mysql.connector import Error
import hashlib


def create_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name
        )
        print("Connection to MySql is successfully!")
    except Error as e:
        print(f"The error '{e}' occurred")
    return connection


def insert_date(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print('Adding of record is done!')
    except Error as e:
        print(f"The error '{e}' occurred")


if __name__ == '__main__':
    salt = 'La 847383 La'
    user_name1 = input('Введите имя пользователя: ')
    password1 = input('Введите пароль: ')
    hash_password1 = hashlib.sha256((password1 + salt).encode())
    print(hash_password1.hexdigest())
    password2 = input('Введите повторно пароль: ')
    hash_password2 = hashlib.sha256((password2 + salt).encode())
    if hash_password1.hexdigest() == hash_password2.hexdigest():
        connection1 = create_connection('localhost', 'root', '', 'sample')
        query1 = f"INSERT INTO users(name, password) VALUES('{user_name1}', '{hash_password1.hexdigest()}');"
        insert_date(connection1, query1)
        print('Все отлично! Пароли совпадают! Пользователь сохранен.')
    else:
        print('Повторный пароль не совпадает.')


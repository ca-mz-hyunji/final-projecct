import pymysql
from pymysql.cursors import DictCursor
import os
from dotenv import load_dotenv

load_dotenv('config/.env.db')

DB_CONFIG = {
    'host': os.environ.get('DB_HOST'),
    'user': os.environ.get('DB_USER'),
    'password': os.environ.get('DB_PASSWORD'),
    'database': os.environ.get('DB_NAME'),
    'port': int(os.environ.get("PORT"))
}

class Connection:

    def get_db_connection():
        return pymysql.connect(**DB_CONFIG, cursorclass=DictCursor)

class UserAuth:
     
    def get_user_data(username, password):
        search_sql = "SELECT * FROM auth_data WHERE username=%s AND password=%s;"
        with Connection.get_db_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(search_sql, (username, password))
                rows = cursor.fetchall()
                if rows:
                    user_data = rows[0]
                    return user_data
                else:
                    return {}

    def check_username(username):
        search_sql = "SELECT * FROM auth_data WHERE username=%s;"
        with Connection.get_db_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(search_sql, (username))
                rows = cursor.fetchall()
                if rows:
                    return True
                else:
                    return False

    def add_new_user(username, password):
        write_sql = "INSERT INTO auth_data (username, password) VALUES (%s, %s)"
        with Connection.get_db_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(write_sql, (username, password))
                connection.commit()
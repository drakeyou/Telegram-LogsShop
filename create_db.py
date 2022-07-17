import pymysql.cursors
from config import HOST, PORT, USER, PASSWORD, DB_NAME

users_scheme = "CREATE TABLE `users`(" \
               "username text," \
               "id int AUTO_INCREMENT NOT NULL PRIMARY KEY," \
               "user_id BIGINT NOT NULL UNIQUE KEY, " \
               "balance BIGINT NOT NULL," \
               "total_earnings BIGINT NOT NULL" \
               ");"

categories_scheme = "CREATE TABLE `categories`(" \
                    "category varchar(32) NOT NULL UNIQUE KEY," \
                    "price int NOT NULL," \
                    "id int AUTO_INCREMENT NOT NULL PRIMARY KEY" \
                    ");"

logs_scheme = "CREATE TABLE `logs`(" \
              "id int AUTO_INCREMENT NOT NULL PRIMARY KEY," \
              "sender_id BIGINT NOT NULL," \
              "category text NOT NULL," \
              "log text NOT NULL," \
              "is_checked BOOL NOT NULL" \
              ");"


def connect(db_name=None):
    try:
        connection_ = pymysql.connect(
            host=HOST,
            port=PORT,
            user=USER,
            password=PASSWORD,
            database=db_name,
            cursorclass=pymysql.cursors.DictCursor
        )

        print("Connection Successful")
        return connection_
    except Exception as err:
        print("Connection was failed")
        print(err)


connection = connect()
cursor = connection.cursor()
cursor.execute(f"CREATE DATABASE {DB_NAME}")
cursor.close()

connection = connect(DB_NAME)
cursor = connection.cursor()

cursor.execute(users_scheme)
cursor.execute(categories_scheme)
cursor.execute(logs_scheme)

cursor.close()

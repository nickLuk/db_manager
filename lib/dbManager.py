import mysql.connector
from mysql.connector import Error
if __name__ == "__main__":
    pass


class Db_manager():

    def __init__(self, host: str, user: str, password: str, database: str):
        try:
            self.__db = mysql.connector.connect(
                host=host,
                user=user,
                password=password,
                database=database
            )
            if self.__db.is_connected():
                print('Connected to MySQL database')
        except Error as e:
            print(e)

    def show_all_users(self):
        cursor = self.__db.cursor()
        cursor.execute("SELECT id, name, surname, age, email, password FROM users")
        result = cursor.fetchall()
        return result

    def add_user(self):
        cursor = self.__db.cursor()
        name = input("Enter user name: ")
        surname = input("Enter user surname: ")
        age = int(input("Enter user age: "))
        email = input("Enter user email: ")
        password = input("Enter user password: ")
        sql = "INSERT INTO users (name, surname, age, email, password) VALUES (%s, %s, %s, %s, %s)"
        value = (name, surname, age, email, password)
        result = cursor.execute(sql, value)
        self.__db.commit()
        print(cursor.rowcount, "record inserted.")
        return result
    
    def check_user(self):
        cursor = self.__db.cursor()
        user_email = input("Enter email: ")
        sql = "SELECT `password` FROM `users` WHERE email=(%s)"
        value = (user_email,)
        cursor.execute(sql, value)
        result = cursor.fetchone()
        return result

    def del_user(self):
        cursor = self.__db.cursor()
        delete = input("Enter ID to delete=====>")
        sql = "DELETE FROM users WHERE id = %s"
        d = (delete,)
        result = cursor.execute(sql, d)
        self.__db.commit()
        print(cursor.rowcount, "record(s) deleted")
        return result










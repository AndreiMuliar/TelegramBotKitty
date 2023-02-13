import sqlite3 as sl
import time


def insert_varible_into_table(user_id):
    try:
        con = sl.connect('telegram_users.db')
        cursor = con.cursor()

        tm = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

        cursor.execute("SELECT user_id FROM users WHERE user_id = ?", (user_id,))
        if cursor.fetchone() is None:
            sqlite_insert_query = """ INSERT INTO users
                                  (user_id, last_request_time)
                                  VALUES
                                  (?, ?); """
            cursor.execute(sqlite_insert_query, (user_id, tm))
        else:
            cursor.execute("Update users set last_request_time = ? where user_id = ?", (tm, user_id))

        con.commit()
        cursor.close()

    except sl.Error as error:
        print(f"Ошибка при работе с SQLite {error}")
    finally:
        if con:
            con.close()


def read_sqlite_table():
    try:
        con = sl.connect('telegram_users.db')
        cursor = con.cursor()
        data = cursor.execute("""SELECT * from users""")
        for row in data:
            print(f"{row[0]}\tID: {row[1]}\tLRT: {row[2]}")

        con.commit()
        cursor.close()

    except sl.Error as error:
        print("Ошибка при работе с SQLite", error)
    finally:
        if con:
            con.close()


if __name__ == '__main__':
    read_sqlite_table()

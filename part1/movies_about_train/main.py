import sqlite3


def main():
    con = sqlite3.connect("../netflix.db")
    cur = con.cursor()
    sqlite_query = "select * from netflix where description like '%train%'"
    cur.execute(sqlite_query)
    # здесь должно быть формирование и вывод списка
    # print(cur.fetchall())
    con.close()


if __name__ == '__main__':
    main()

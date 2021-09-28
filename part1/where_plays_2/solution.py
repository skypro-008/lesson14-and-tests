import sqlite3


def main():
    con = sqlite3.connect("../netflix.db")
    cur = con.cursor()
    sqlite_query = ("SELECT title, rating FROM netflix "
                    "WHERE [cast] LIKE 'Joaquin Phoenix%'"
                    "AND type='Movie'")
    cur.execute(sqlite_query)
    for row in cur.fetchall():
        title = row[0]
        rating = row[1]
        print(f'{title} — {rating}')
    con.close()


if __name__ == '__main__':
    main()

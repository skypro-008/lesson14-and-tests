import sqlite3


def main():
    con = sqlite3.connect("../netflix.db")
    cur = con.cursor()
    sqlite_query = ("SELECT title, release_year FROM netflix "
                    "WHERE release_year BETWEEN 1943 AND 1945 "
                    "AND type='Movie'")
    cur.execute(sqlite_query)
    for row in cur.fetchall():
        title = row[0]
        year = row[1]
        print(f'{title} — {year}')
    con.close()


if __name__ == '__main__':
    main()

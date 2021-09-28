import sqlite3


def main():
    con = sqlite3.connect("../netflix.db")
    cur = con.cursor()
    sqlite_query = ("SELECT [title], [cast] FROM netflix "
                    "WHERE director='Guy Ritchie' AND release_year <= 2000 "
                    "AND type='Movie'")
    cur.execute(sqlite_query)
    for row in cur.fetchall():
        title = row[0]
        cast = row[1]
        print(f'{title}: {cast}')
    con.close()


if __name__ == '__main__':
    main()

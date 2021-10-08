import sqlite3
import prettytable

con = sqlite3.connect("../netflix.db")
cur = con.cursor()
sqlite_query = ("SELECT `title`, "
                "strftime('%d.%m.%Y', MAX(date_added)) AS last_date "
                "FROM netflix ")
result = cur.execute(sqlite_query)
result = cur.fetchall()
movie_title = result[0][0]
add_date = result[0][1]
result = (f'{movie_title} — {add_date}')
con.close()

if __name__ == '__main__':
    print(result)

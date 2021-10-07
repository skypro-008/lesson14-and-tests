import sqlite3

con = sqlite3.connect("../netflix.db")
cur = con.cursor()
sqlite_query = ("SELECT director, COUNT(director) "
                "FROM netflix "
                "WHERE country LIKE '%United States%' "
                "GROUP BY director "
                "ORDER BY COUNT(director) DESC "
                "LIMIT 15")  # TODO измените код запроса
result = ''
cur.execute(sqlite_query)
for row in cur.fetchall():
    director = row[0]
    count = row[1]
    result += (f'{director}: {count} фильмов\n')
con.close()

if __name__ == '__main__':
    print(result)

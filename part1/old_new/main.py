import sqlite3
import prettytable

con = sqlite3.connect("../netflix.db")
cur = con.cursor()

# TODO измените код запроса


sqlite_query = ("SELECT [title], [cast] FROM netflix "
                    "WHERE director='Guy Ritchie' AND release_year <= 2000 "
                    "AND type='Movie'")

result = cur.execute(sqlite_query)


# не удаляйте код дальше, он нужен для вывода результата
# запроса в красивом формате

    
mytable = prettytable.from_db_cursor(result)
mytable.max_width = 30


if __name__ == '__main__':
    print(mytable)

import sqlite3


def main():
    con = sqlite3.connect("../netflix.db")
    cur = con.cursor()
    sqlite_query = ("SELECT director, COUNT(director) "
                    "FROM netflix "
                    "WHERE country LIKE '%United States%' "
                    "AND director IS NOT NULL "
                    "GROUP BY director")
    cur.execute(sqlite_query)
    for row in cur.fetchall():
        director = row[0]
        count = row[1]
        word = get_word_ending(count)
        print(f'{director}: {count} {word}')
    con.close()


def get_word_ending(x):
    if x == 1 or int(str(x)[-1]) == 1:
        return 'фильм'
    elif x in [11, 12, 13, 14]:
        return 'фильмов'
    elif x in [2, 3, 4] or int(str(x)[-1]) in [2, 3, 4]:
        return 'фильма'
    else:
        return 'фильмов'


if __name__ == '__main__':
    main()

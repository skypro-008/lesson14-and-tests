from tools import task_preparing


@task_preparing(limit=20)  # Лимит количества выводимых строк
def main():
    sqlite_query = ("SELECT title, release_year FROM netflix "
                    "WHERE release_year BETWEEN 1943 AND 1945 "
                    "AND type='Movie'")
    return sqlite_query


if __name__ == '__main__':
    main()


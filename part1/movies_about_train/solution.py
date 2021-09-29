from tools import task_preparing


@task_preparing(limit=20)  # Лимит количества выводимых строк
def main():
    sqlite_query = ("SELECT title FROM netflix "
                    "WHERE description LIKE '%train%' "
                    "AND type='Movie'")
    return sqlite_query

if __name__ == '__main__':
    main()

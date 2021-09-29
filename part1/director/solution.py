from tools import task_preparing


@task_preparing(limit=20)  # Лимит количества выводимых строк
def main():
    sqlite_query = ("SELECT DISTINCT director "
                    "FROM netflix ")
    return sqlite_query


if __name__ == '__main__':
    main()

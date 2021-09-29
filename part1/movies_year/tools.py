import sqlite3
import re
import prettytable

def task_preparing(limit=10):
    def decorator(student_func):
        def wrapper(*args, **kwargs):
            con = sqlite3.connect("../netflix.db")
            cur = con.cursor()
            print('ШАПКА ТАБЛИЦЫ В БД, основные поля:')
            pre_create_query = 'SELECT country, director, title, release_year, type, [cast] FROM netflix LIMIT 3'
            pre_query = cur.execute(pre_create_query)
            table = prettytable.from_db_cursor(pre_query)
            table.max_width = 30
            print(table)
            query_limit = student_func()
            if query_limit[-1] == ';':
                query_limit = query_limit[:-1]
            query = student_func()
            rows_counter = f'SELECT count(*) FROM ({query})'
            number_of_rows = cur.execute(rows_counter).fetchall()[0][0]
            query_limit += f' LIMIT {limit}'
            print('ОТВЕТ НА ЗАПРОС:')
            result = cur.execute(query_limit)
            mytable = prettytable.from_db_cursor(result)
            print(mytable)
            print(f'ВЫДАЧА ОГРАНИЧЕНА {limit} СТРОКАМИ')
            print(f'ОБЩЕЕ ЧИСЛО СТРОК: {number_of_rows}')
            student_result = cur.execute(query)
            con.close()
            return {'structure': sql_checker(student_func())[0],
                    'keywords': sql_checker(student_func())[1],
                    'number_of_rows': number_of_rows, 
                    'query_result': student_result}
        return wrapper
    return decorator

def sql_checker(query: str):
    query = query.lower()
    keywords = get_key_words(query)
    select_ind = query.find('select ')
    from_ind = query.find('from ')
    where_ind = query.find('where ')
    and_ind = query.find('and ')
    select_block = query[select_ind:from_ind]
    from_block = query[from_ind:where_ind]
    where_block = query[where_ind:]
    and_block = None
    if and_ind:
        where_block = query[where_ind:and_ind]
        and_block = query[and_ind:]
    blocks = {'колонка':select_block, 
              'таблица': from_block, 
              'условие': where_block,
              'доп условие': and_block}
    for key, value in blocks.items():
        blocks[key] = cleaner(blocks[key])
    return blocks, keywords


def cleaner(lst):
    lst = lst.split(' ')
    key_words = ['select', 'from', 'where', 'like', 'distinct', 'and', '']
    for value in key_words:
        if value in lst:
            lst.remove(value)
    for value in lst:
        if ',' in value:
            devided_value = value.split(',')
            try:
                devided_value.remove('')
            except:
                pass
            lst.remove(value)
            lst += devided_value
    return lst
            
def get_key_words(query):
    keywords = ['select', 'from', 'where', 'like', 'group by', 'distinct']
    lst = []
    for keyword in keywords:
        if keyword in query:
            lst.append(keyword)
    return lst
    

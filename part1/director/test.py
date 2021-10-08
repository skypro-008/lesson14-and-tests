import unittest
import main
import solution
from tools import SkyproTestCase


class DirectorsTestCase(SkyproTestCase):
    def setUp(self):
        self.student_query = self.get_query_info(main.sqlite_query)
        self.author_query = self.get_query_info(solution.sqlite_query)

    def test_query_structure_has_distinct_method(self):
        keywords = self.student_query.get('query_info').get('keywords')
        self.assertIn('distinct', keywords,
                      ('%@Проверьте, что в результате запроса'
                       'не повторяются имена режисеров'))

    def test_query_has_limit(self):
        count = self.student_query.get('cursor_info').get('rows_count')
        self.assertEqual(count, 10,
                         '%@Проверьте, что ограничили запрос '
                         'десятью значениями')

    def test_query_columns_is_correct(self):
        student_columns = self.student_query.get('cursor_info').get('columns')
        author_columns = self.author_query.get('cursor_info').get('columns')
        self.assertEqual(student_columns, author_columns,
                         ('%@Проверьте, что правильно выбрали'
                          ' колонку в базе данных. '
                          f'Вы выбрали {student_columns}, тогда '
                          f'как необходимо {author_columns}'))

    def test_query_result_havent_null_values(self):
        student_result = self.student_query.get(
            'cursor_info').get('query_result')
        self.assertNotIn((None,), student_result,
                         ('%@Проверьте, что исключили из выдачи '
                          'значение None'))

    def test_result_in_correct_order(self):
        student_result = self.student_query.get(
            'cursor_info').get('query_result')
        author_result = self.author_query.get(
            'cursor_info').get('query_result')
        self.assertEqual(student_result, author_result,
                         '%@Проверьте, что отсортировали результат запроса в '
                         'алфавитном порядке')


if __name__ == "__main__":
    unittest.main()

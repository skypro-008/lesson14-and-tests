import unittest
import main
import solution
from tools import SkyproTestCase


class TrainTestCase(SkyproTestCase):
    def setUp(self):
        self.student_query = self.get_query_info(main.sqlite_query)
        self.author_query = self.get_query_info(solution.sqlite_query)

    def test_query_structure_has_like_operator(self):
        keywords = self.student_query.get('query_info').get('keywords')
        self.assertTrue('like' in keywords,
                        ('%@Проверьте, что воспользовались оператором like'
                         ' при составлении запроса'))

    def test_operator_like_has_correct_value(self):
        conditions = self.student_query.get('query_info').get('условие')
        value = ' '.join(conditions)
        self.assertRegex(value, ".%train%",
                         ('%@Проверьте, что задали правильное условие поиска '
                          'после оператора LIKE в запросе'))

    def test_tv_show_is_excluded(self):
        student_result = self.student_query.get(
            'cursor_info').get('query_result')
        self.assertNotIn(('The Letter for the King',), student_result,
                         ('%@Проверьте, что исключили из выдачи '
                          'сериалы'))

    def test_query_columns_is_correct(self):
        student_columns = self.student_query.get('cursor_info').get('columns')
        author_columns = self.author_query.get('cursor_info').get('columns')
        self.assertEqual(student_columns, author_columns,
                         ('%@Проверьте, что правильно выбрали'
                          ' колонку в базе данных. '
                          f'Вы выбрали {student_columns}, тогда '
                          f'как необходимо {author_columns}'))

    def test_rows_count_superfluous_condition(self):
        count = self.student_query.get('cursor_info').get('rows_count')
        author_count = self.author_query.get('cursor_info').get('rows_count')
        self.assertFalse(count > author_count,
                         ('%@Кажется, в запросе имеется лишнее условие.'
                          f'Выводится больше строк ({count}) '
                          f'чем предполагалось {author_count}'))

    def test_rows_count_lack_condition(self):
        count = self.student_query.get('cursor_info').get('rows_count')
        author_count = self.author_query.get('cursor_info').get('rows_count')
        self.assertFalse(count < author_count,
                         ('%@Кажется, в запросе нехватает условия.'
                          f'Выводится меньше строк ({count}) '
                          f'чем предполагалось {author_count}'))


if __name__ == "__main__":
    unittest.main()

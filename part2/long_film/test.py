import unittest
import main
import solution
from tools import SkyproTestCase
import re


class YearsTestCase(SkyproTestCase):
    def setUp(self):
        self.student_query = self.get_query_info(main.sqlite_query)
        self.author_query = self.get_query_info(solution.sqlite_query)

    def test_main_has_result(self):
        self.assertTrue(hasattr(main, 'result'),
                        r'%@Проверьте, что переменная result существует')

    def test_result_format_is_correct(self):
        self.assertRegex(
            main.result,
            r'(/w+)*\s[\-—]\s[0-9]*\sминут',
            r'%@Проверьте, что используете правильный формат выдачи')

    def test_query_exists_year_condition(self):
        value = re.findall(r"\d+", main.sqlite_query)
        author_value = re.findall(r"\d+", solution.sqlite_query)
        self.assertEqual(
            value, author_value,
            (r'%@Проверьте, на самом ли деле это '
             'самый длинный фильм 2019 года.'))

    def test_duration_value_is_correct(self):
        value = re.findall(r"\d+", main.result)
        author_value = re.findall(r"\d+", solution.result)
        self.assertEqual(
            value, author_value,
            (r'%@Проверьте, на самом ли деле это '
             'самый длинный фильм 2019 года.'))


if __name__ == "__main__":
    unittest.main()

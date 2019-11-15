import unittest
import data_manager

from application import application
from company import company
from position import position
from students import students

def compare_lists(tester, expected_list, result_list):
    if len(expected_list) == 0 and len(result_list) == 0:
        return
    
    if len(expected_list) != 0 and len(result_list) == 0:
        tester.assertListEqual(result_list, expected_list)

    for item in result_list:
        tester.assertTrue(item in expected_list)


def check_forbidden_functions(tester, file_name):
    with open(file_name, 'r') as f:
        lines = f.read()
        tester.assertEqual(lines.find('find('), -1)
        tester.assertEqual(lines.find('sort('), -1)
        tester.assertEqual(lines.find('sorted('), -1)
        tester.assertEqual(lines.find('sum('), -1)
        tester.assertEqual(lines.find('count('), -1)
        tester.assertEqual(lines.find('index('), -1)
        tester.assertEqual(lines.find('print('), -1)


class StudentTester(unittest.TestCase):

    def test_forbidden_functions(self):
        check_forbidden_functions(self, 'students/students.py')

    def test_delete_student(self):
        table = data_manager.get_table_from_file('students/test_students_data.csv')
        expected = data_manager.get_table_from_file('students/test2_students_data.csv')
        result = students.delete_student(table, 'i3[*1Hl0')
        compare_lists(self, expected, result)


class ApplicationTester(unittest.TestCase):

    def test_forbidden_functions(self):
        check_forbidden_functions(self, 'application/application.py')


class CompanyTester(unittest.TestCase):

    def test_forbidden_functions(self):
        check_forbidden_functions(self, 'company/company.py')

    def test_delete_company(self):
        table = data_manager.get_table_from_file('company/test_company_data.csv')
        expected = data_manager.get_table_from_file('company/test2_company_data.csv')
        result = students.delete_student(table, '6Hy#4dL1')
        compare_lists(self, expected, result)


class PositionTester(unittest.TestCase):

    def test_forbidden_functions(self):
        check_forbidden_functions(self, 'position/position.py')

        
def main():
    unittest.main(verbosity=2)


if __name__ == "__main__":
    main()







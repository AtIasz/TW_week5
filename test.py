import unittest
import data_manager

from application import application
from company import company
from position import position
from students import students


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
        tester.assertEqual(lines.find('input('), -1)


class StudentTester(unittest.TestCase):

    def test_forbidden_functions(self):
        check_forbidden_functions(self, 'students/students.py')


def main():
    unittest.main(verbosity=2)


if __name__ == "__main__":
    main()







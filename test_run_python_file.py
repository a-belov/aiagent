import unittest
from functions.run_python_file import run_python_file


class TestRunPythonFile(unittest.TestCase):
    def setUp(self):
        self.run_python_file = run_python_file

    def test_run_1(self):
        result = self.run_python_file("calculator", "main.py")
        print(result)

    def test_run_2(self):
        result = self.run_python_file("calculator", "main.py", ["3 + 5"])
        print(result)

    def test_run_3(self):
        result = self.run_python_file("calculator", "tests.py")
        print(result)     

    def test_run_4(self):
        result = self.run_python_file("calculator", "../main.py")
        print(result)

    def test_run_5(self):
        result = self.run_python_file("calculator", "nonexistent.py")
        print(result)

    def test_run_6(self):
        result = self.run_python_file("calculator", "lorem.txt")
        print(result) 

if __name__ == "__main__":
    unittest.main()
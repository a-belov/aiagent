import unittest
from functions.get_file_content import get_file_content


class TestGetFileContent(unittest.TestCase):
    def setUp(self):
        self.get_file_content = get_file_content

    def test_get_lorem_ipsum(self):
        result = self.get_file_content("calculator", "lorem.txt")
        print(f"lorem.txt length: {len(result)}")
        print(f"lorem.txt truncated: {'truncated' in result}")

    def test_get_calc_py(self):
        result = self.get_file_content("calculator", "pkg/calculator.py")
        print(result)

    def test_get_mainpy(self):
        result = self.get_file_content("calculator", "main.py")
        print(result)     

    def test_get_calc_bin(self):
        result = self.get_file_content("calculator", "/bin/cat")
        print(result)

    def test_get_calc_ne(self):
        result = self.get_file_content("calculator", "pkg/does_not_exist.py")
        print(result)

if __name__ == "__main__":
    unittest.main()
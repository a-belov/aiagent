import unittest
from functions.write_file import write_file


class TestWriteFile(unittest.TestCase):
    def setUp(self):
        self.write_file = write_file

    def test_write_1(self):
        result = self.write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
        print(result)

    def test_write_2(self):
        result = self.write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
        print(result)

    def test_write_3(self):
        result = self.write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
        print(result)     

if __name__ == "__main__":
    unittest.main()
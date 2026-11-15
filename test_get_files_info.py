import unittest
from functions.get_files_info import get_files_info

class TestGetFilesInfo(unittest.TestCase):
    def setUp(self):
        self.get_files_info = get_files_info

    def test_calc_root(self):
        result = self.get_files_info("calculator", ".")
        print(f'Result for current directory:\n{result}')
#         self.assertEqual(result, '''Result for current directory:
#   - main.py: file_size=719 bytes, is_dir=False
#   - tests.py: file_size=1331 bytes, is_dir=False
#   - pkg: file_size=44 bytes, is_dir=True''')

    def test_calc_pkg(self):
        result = self.get_files_info("calculator", "pkg")
        print(f'Result for \'pkg\' directory:\n{result}')
#         self.assertEqual(result, '''Result for 'pkg' directory:
#   - calculator.py: file_size=1721 bytes, is_dir=False
#   - render.py: file_size=376 bytes, is_dir=False''')

    def test_calc_bin(self):
        result = self.get_files_info("calculator", "/bin")
        print(f'Result for \'/bin\' directory:\n{result}')
    #     self.assertEqual(result, '''Result for '/bin' directory:
    # Error: Cannot list "/bin" as it is outside the permitted working directory''')

    def test_calc_parent(self):
        result = self.get_files_info("calculator", "../")
        print(f'Result for \'../\' directory:\n{result}')
    #     self.assertEqual(result, '''Result for '../' directory:
    # Error: Cannot list "../" as it is outside the permitted working directory''')


if __name__ == "__main__":
    unittest.main()
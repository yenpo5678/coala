import unittest
from queue import Queue
from unittest.mock import MagicMock

# 引入 Bear 與必要依賴
from coalib.bears.Bear import Bear
from coalib.settings.Section import Section

class BrokenBear(Bear):
    """一個故意會壞掉的 Bear，用來測試錯誤處理邏輯"""
    def run(self, *args, **kwargs):
        raise ValueError("Something went wrong inside the bear!")

    @staticmethod
    def kind():
        return 'local'

class TestBearRefactoring(unittest.TestCase):
    def setUp(self):
        self.section = Section("test_section")
        self.queue = Queue()
        self.bear = BrokenBear(self.section, self.queue)

    def test_execute_handles_exception_before_refactoring(self):
        results = self.bear.execute("test_file.py")
        
        self.assertIsNone(results)
        
        print("\n[PASS] Bear.execute() caught the exception (returned None as expected).")

    def test_execute_handles_exception_after_refactoring(self):
        results = self.bear.execute("test_file.py")
        
        self.assertEqual(results, [])
        print("\n[PASS] Refactored execute() returns [] correctly (Bug Fixed!).")

if __name__ == '__main__':
    unittest.main()
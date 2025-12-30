import unittest
from coalib.results.Result import Result, SourceLocation

class TestResultRefactoring(unittest.TestCase):
    """
    展示 Refactoring 前後的差異。
    """

    def setUp(self):
        # 共用的測試資料
        self.origin = "TestOrigin"
        self.msg = "Refactoring Test"
        self.file = "main.py"
        self.line = 10
        self.col = 5
        self.end_line = 10
        self.end_col = 20

    def test_initialization_before_refactoring(self):
        """
        [Before] 重構前：必須傳遞大量分散的參數 (Data Clump)
        """
        result = Result.from_values(
                        origin=self.origin,
                        message=self.msg,
                        file=self.file,         # 參數 1
                        line=self.line,         # 參數 2
                        column=self.col,        # 參數 3
                        end_line=self.end_line, # 參數 4
                        end_column=self.end_col # 參數 5
                        )
        self.assertEqual(result.message, self.msg)
        print("\n[PASS] Before Refactoring: Created Result with long parameter list.")

    def test_initialization_after_refactoring(self):
        """
        [After] 重構後：使用參數物件 (Parameter Object)
        """
        loc = SourceLocation(self.file, self.line, self.col, self.end_line, self.end_col)
        
        result = Result.from_location(
                        origin=self.origin,
                        message=self.msg,
                        location=loc
                        )

        # 驗證結果與重構前一致 (Regression Testing)
        self.assertEqual(result.message, self.msg)
        self.assertEqual(result.affected_code[0].start.line, self.line)
        self.assertEqual(result.affected_code[0].start.column, self.col)
        
        print("[PASS] After Refactoring: Successfully created Result using SourceLocation object.")

if __name__ == '__main__':
    unittest.main()
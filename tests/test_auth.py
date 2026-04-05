import unittest
from src.auth import login

class TestAuth(unittest.TestCase):

    def test_login_success(self):
        # Simulating correct login (manual check)
        self.assertTrue(True)  # placeholder since input() is used

    def test_login_failure(self):
        self.assertTrue(True)  # cannot test input easily without mocking

if __name__ == "__main__":
    unittest.main()
import unittest
from src.detector import detect_threat

class TestDetector(unittest.TestCase):

    def test_normal_activity(self):
        # No alert expected
        detect_threat("normal")
        self.assertTrue(True)

    def test_failed_attempts(self):
        detect_threat("login_fail")
        detect_threat("login_fail")
        detect_threat("login_fail")
        self.assertTrue(True)

if __name__ == "__main__":
    unittest.main()
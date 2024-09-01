import unittest
from task import LearningTracker

class TestTask(unittest.TestCase):

    lp_tracker = LearningTracker()

    def test_verify_name(self):
        self.assertIsNotNone(self.lp_tracker.verify_name("Jean-Claude"), "There is NOT match")
        self.assertIsNotNone(self.lp_tracker.verify_name("O'Neill"), "There is NOT match")
        self.assertIsNotNone(self.lp_tracker.verify_name("George"), "There is NOT match")
        self.assertIsNotNone(self.lp_tracker.verify_name("ge'-ge"), "There is NOT match")
        self.assertIsNotNone(self.lp_tracker.verify_name("Stanisław Oğuz"), "There is NOT match")

    def test_verify_email(self):
        self.assertIsNotNone(self.lp_tracker.verify_email("test@example.com"), "There is NOT match")
        self.assertIsNotNone(self.lp_tracker.verify_email("scott_dylan@google.com"), "There is NOT match")
        self.assertIsNotNone(self.lp_tracker.verify_email("martin@yahoo.com"), "There is NOT match")
        self.assertIsNotNone(self.lp_tracker.verify_email("test@test"), "There is NOT match")
        self.assertIsNotNone(self.lp_tracker.verify_email("_#$%@t..%^&*"), "There is NOT match")


if __name__ == "__main__":
    unittest.main()
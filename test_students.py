import unittest
from Students import *

class TestStudent(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add_student(1, "Siya"), "Student Added")

    def test_search(self):
        add_student(2, "Rahul")
        self.assertEqual(search_student(2), "Rahul")

    def test_search_not_found(self):
        self.assertEqual(search_student(100), "Student Not Found")

    def test_update(self):
        add_student(3, "Priya")
        update_student(3, "Anjali")
        self.assertEqual(search_student(3), "Anjali")

    def test_update_not_found(self):
        self.assertEqual(update_student(50, "Test"), "Student Not Found")

if __name__ == "__main__":
    unittest.main()
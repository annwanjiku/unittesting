import  unittest
from code import converttoabs

class TestForAbs(unittest.TestCase):
    def test_positive_number(self):
        self.assertEqual(converttoabs(5),5)
    def test_negative_number(self):
        self.assertEqual(converttoabs(-10),10)
    def test_zero(self):
        self.assertEqual(converttoabs(0),0)
    def test_num_string(self):
        self.assertEqual(converttoabs("5"),5)
    def test_actual_string(self):
        with self.assertRaises(ValueError):
            converttoabs("b")

if __name__ == "__main__":
    unittest.main()

import unittest
from str_sum import add

class TestSum(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        return super().setUpClass()
    
    def test_add(self):
        outp = add(r'//;\n1\n2;4\n3')
        self.assertEqual(outp,10)

        outp = add(r'//;\n1\n2;4\n3;-5;-1;-4')
        self.assertEqual(outp,0)

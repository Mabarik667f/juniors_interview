import unittest


from solution import strict

@strict
def sum_two(a: int, b: float) -> float:
    return a + b


class TestCasesForStrictDec(unittest.TestCase):
    
    def test_args_for_two_sum(self):
        self.assertEqual(sum_two(2, 2.0), 4)
        self.assertRaises(TypeError, sum_two, 2, "2")
        self.assertRaises(TypeError, sum_two, 3.0, "2")

    def test_kwargs_for_two_sum(self):
        self.assertEqual(sum_two(a=2, b=2.0), 4)
        self.assertRaises(TypeError, sum_two, a="2", b=2.0)
        self.assertRaises(TypeError, sum_two, a=True, b=2)

    def test_args_and_kwargs_for_two_sum(self):
        self.assertEqual(sum_two(8, b=8.0), 16)
        self.assertRaises(TypeError, sum_two, 2.0, b=2)
        self.assertRaises(TypeError, sum_two, 2, b="2.0")


if __name__ == "__main__":
    unittest.main()

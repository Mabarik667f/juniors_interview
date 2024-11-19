import unittest
import csv 
from solution import main

class TestCasesForTask2(unittest.IsolatedAsyncioTestCase):


    async def test_script(self):
        await main()
        with open("res.csv", newline="") as f:
            reader = csv.reader(f)
            for row in reader:
                self.assertEqual(row[1], '1286')
                break


if __name__ == "__main__":
    unittest.main()

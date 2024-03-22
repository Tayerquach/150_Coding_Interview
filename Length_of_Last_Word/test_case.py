import unittest
from Solution import Solution

class LengthOfLastWord(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_case(self):
        s = Solution()
        for input, result in [("Hello World", 5), 
                              ("   fly me   to   the moon  ", 4),
                              ("luffy is still joyboy", 6)]:
            self.assertEqual(s.lengthOfLastWord(input), result)

if __name__ == "__main__":
    unittest.main()
            

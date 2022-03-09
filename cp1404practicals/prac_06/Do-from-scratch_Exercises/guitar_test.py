from guitar import Guitar
import unittest


class TestGuitar(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.gibson = Guitar("Gibson L-5 CES", 1922, 16035.40)
        cls.another = Guitar("Another Guitar", 2015, 100.0)

    def test_get_age(self):
        self.assertEqual(self.gibson.get_age(), 100)
        self.assertEqual(self.another.get_age(), 7)

    def test_is_vintage(self):
        self.assertEqual(self.gibson.is_vintage(), True)
        self.assertEqual(self.another.is_vintage(), False)


if __name__ == "__main__":
    unittest.main()

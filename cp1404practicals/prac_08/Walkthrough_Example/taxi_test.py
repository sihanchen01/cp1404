from taxi import Taxi
import unittest


class TestTaxi(unittest.TestCase):
    def setUp(self) -> None:
        self.taxi = Taxi(name="Prius 1", fuel=100)

    def test_current_fare(self):
        self.taxi.drive(40)
        print(str(self.taxi))
        print(f"Current fare: {self.taxi.get_fare()}")
        self.assertEqual(self.taxi.get_fare(), 40*1.23)

    def test_reset_fare(self):
        print()
        self.taxi.drive(40)
        self.taxi.start_fare()
        self.taxi.drive(100)
        print(str(self.taxi))
        print(f"Current fare: {self.taxi.get_fare()}")
        self.assertEqual(self.taxi.get_fare(), 60*1.23)


if __name__ == "__main__":
    unittest.main()

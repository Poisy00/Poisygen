import unittest

from poisygen import parse_random_address


class TestAddressParser(unittest.TestCase):
    SAMPLE_HTML = (
        "<span><b>Street:</b>&nbsp;&nbsp;123 Main Street</span>"
        "<span><b>City:</b>&nbsp;&nbsp;Springfield</span>"
        "<span><b>State/province/area: </b>&nbsp;&nbsp;Illinois</span>"
        "<span><b>Zip code:</b>&nbsp;&nbsp;62704</span>"
    )

    def test_parse_random_address(self) -> None:
        parsed = parse_random_address(self.SAMPLE_HTML)
        self.assertEqual(parsed["Street"], "123 Main Street")
        self.assertEqual(parsed["City"], "Springfield")
        self.assertEqual(parsed["State/province/area"], "Illinois")
        self.assertEqual(parsed["Zip code"], "62704")


if __name__ == "__main__":
    unittest.main()

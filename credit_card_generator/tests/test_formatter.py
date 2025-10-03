import json
import unittest

from poisygen import format_csv, format_json, format_pipe, format_plain

SAMPLE = [
    {"number": "4111111111111111", "exp_month": "01", "exp_year": "30", "cvv": "123"},
    {"number": "5555555555554444", "exp_month": "06", "exp_year": "28", "cvv": "321"},
]


class TestFormatter(unittest.TestCase):
    def test_format_plain(self) -> None:
        rendered = format_plain(SAMPLE)
        lines = rendered.splitlines()
        self.assertEqual(lines[0], SAMPLE[0]["number"])
        self.assertEqual(lines[1], SAMPLE[1]["number"])

    def test_format_pipe(self) -> None:
        rendered = format_pipe(SAMPLE)
        self.assertIn("4111111111111111|01|30|123", rendered)
        self.assertIn("5555555555554444|06|28|321", rendered)

    def test_format_csv(self) -> None:
        rendered = format_csv(SAMPLE)
        self.assertTrue(rendered.startswith("card_number,exp_month,exp_year,cvv"))
        self.assertIn("4111111111111111,01,30,123", rendered)

    def test_format_json(self) -> None:
        rendered = format_json(SAMPLE)
        parsed = json.loads(rendered)
        self.assertEqual(parsed[0]["number"], SAMPLE[0]["number"])
        self.assertEqual(parsed[1]["cvv"], SAMPLE[1]["cvv"])


if __name__ == "__main__":
    unittest.main()

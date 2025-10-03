import unittest

from poisygen import luhn_checksum, validate_luhn


class TestValidator(unittest.TestCase):
    def test_luhn_checksum(self) -> None:
        self.assertEqual(luhn_checksum("7992739871"), 3)
        self.assertEqual(luhn_checksum("411111111111111"), 1)

    def test_validate_luhn_valid_numbers(self) -> None:
        valid_cards = [
            "4111111111111111",
            "5555555555554444",
            "378282246310005",
        ]
        for card in valid_cards:
            with self.subTest(card=card):
                self.assertTrue(validate_luhn(card))

    def test_validate_luhn_invalid_numbers(self) -> None:
        invalid_cards = [
            "4111111111111112",
            "5555555555554440",
            "378282246310000",
            "abcdefg",
            "",
        ]
        for card in invalid_cards:
            with self.subTest(card=card):
                self.assertFalse(validate_luhn(card))

    def test_checksum_rejects_non_digits(self) -> None:
        with self.assertRaises(ValueError):
            luhn_checksum("1234x")


if __name__ == "__main__":
    unittest.main()

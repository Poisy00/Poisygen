import unittest

from poisygen import CardGenerator, detect_card_type, validate_luhn


class TestCardGenerator(unittest.TestCase):
    def setUp(self) -> None:
        self.generator = CardGenerator()

    def test_generate_from_bin_produces_valid_card(self) -> None:
        card = self.generator.generate_from_bin("445566", length=16)
        self.assertTrue(card.startswith("445566"))
        self.assertEqual(len(card), 16)
        self.assertTrue(validate_luhn(card))

    def test_generate_from_pattern_respects_length(self) -> None:
        card = self.generator.generate_from_bin("378282xxxxxxxxx")
        self.assertEqual(len(card), 15)
        self.assertTrue(card.startswith("378282"))
        self.assertTrue(validate_luhn(card))

    def test_generate_bulk_uniqueness(self) -> None:
        cards = self.generator.generate_bulk("555555", count=20, length=16)
        numbers = [card["number"] for card in cards]
        self.assertEqual(len(numbers), len(set(numbers)))
        for card in cards:
            self.assertTrue(validate_luhn(card["number"]))

    def test_generate_bulk_custom_expiry(self) -> None:
        cards = self.generator.generate_bulk(
            "601100",
            count=5,
            length=16,
            expiry_month=12,
            expiry_year=2030,
        )
        for card in cards:
            self.assertEqual(card["exp_month"], "12")
            self.assertEqual(card["exp_year"], "30")

    def test_generate_cvv_override(self) -> None:
        cvv = self.generator.generate_cvv(card_type="amex", length_override=3)
        self.assertEqual(len(cvv), 3)
        self.assertTrue(cvv.isdigit())

    def test_detect_card_type(self) -> None:
        self.assertEqual(detect_card_type("411111"), "visa")
        self.assertEqual(detect_card_type("555555"), "mastercard")
        self.assertEqual(detect_card_type("378282"), "amex")
        self.assertEqual(detect_card_type("601100"), "discover")
        self.assertEqual(detect_card_type("999999"), "unknown")


if __name__ == "__main__":
    unittest.main()

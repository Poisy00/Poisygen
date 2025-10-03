"""Compatibility wrapper exposing Luhn helpers from the single-file script."""

from poisygen import luhn_checksum, validate_luhn

__all__ = ["luhn_checksum", "validate_luhn"]

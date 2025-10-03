# Namsogen-Style BIN Credit Card Generator (By Poisy)

`poisygen.py` is a single-file, zero-dependency CLI for generating Luhn-valid test card data from BIN patterns. The project is created and maintained by **Poisy**; all rights reserved. Use it to populate QA environments without touching real accounts.

## Download-and-run One-Liners

PowerShell (Windows):

```powershell
irm https://raw.githubusercontent.com/Poisy00/Poisygen/main/poisygen.py | python -
```

curl (macOS/Linux):

```bash
curl -sSL https://raw.githubusercontent.com/Poisy00/Poisygen/main/poisygen.py | python -
```

To save the script locally first:

```powershell
irm https://raw.githubusercontent.com/Poisy00/Poisygen/main/poisygen.py -OutFile poisygen.py
python poisygen.py --interactive
```

Replace the GitHub URL with your hosting location if different.

## Quick Start

```bash
python poisygen.py --bin 445566 --count 50 --format pipe
```

```bash
python poisygen.py --bin 378282 --length 15 --count 25 --format json --output amex.json
```

```bash
python poisygen.py --interactive
```

## Features

- Accepts BINs (6-9 digits) and BIN patterns with `x` placeholders.
- Generates 13–19 digit card numbers that always pass Luhn checks.
- Provides random CVV codes (3 digits or 4 digits for Amex) with override support.
- Produces expiry dates from the current month up to 5 years in the future (or fixed expiry).
- Supports bulk generation with guaranteed uniqueness per batch.
- Outputs in plain text, pipe-delimited, CSV, or JSON formats.
- Interactive mode collects options via prompts.
- Built-in `--self-test` harness runs sanity checks without external dependencies.

## CLI Reference

```bash
python poisygen.py --bin <pattern> [options]
```

| Option | Description |
| ------ | ----------- |
| `--bin`, `-b` | BIN or BIN pattern (digits and `x`). Required unless `--interactive`. |
| `--count`, `-c` | Number of cards to generate (default 10). |
| `--length`, `-l` | Total card length (13-19). Defaults per pattern. |
| `--format`, `-f` | Output format: `plain`, `pipe`, `csv`, or `json`. |
| `--output`, `-o` | Optional file path for the results. |
| `--cvv-length` | Force 3 or 4 digit CVVs. |
| `--expiry-month` / `--expiry-year` | Fix expiry date (must provide both). |
| `--years-ahead` | Cap random expiry generation window (default 5). |
| `--interactive`, `-i` | Launch interactive prompts for all options. |
| `--self-test` | Run embedded unit tests and exit. |

## Legal & Ethical Use

> **WARNING**: Generated numbers are for development and QA testing only. They have no monetary value and cannot be used for real transactions.
>
> Misusing synthetic card numbers for fraudulent activity is illegal. Ensure you comply with local regulations before using this tool.
>
> Tool ownership: Poisy retains all rights and provides the script strictly for lawful testing purposes.

The script avoids real BIN databases or personally identifiable information.

## Project Layout

```
.
+-- poisygen.py        # Standalone CLI script by Poisy
+-- credit_card_generator/
    +-- README.md      # This guide
    +-- tests/         # Unit tests that exercise poisygen.py
```


# Repository Guidelines

## Project Structure & Module Organization
- `poisygen.py`: single-file CLI with generator, formatters, interactive prompts, and embedded self-tests.
- `credit_card_generator/`: compatibility wrappers, CLI shim, README, and unit tests.
- `credit_card_generator/tests/`: unittest-based coverage for validator, generator, and formatters; add new suites here.

## Build, Test, and Development Commands
- `python poisygen.py --bin 445566 --count 5`: run the generator directly from the repo.
- `python -m unittest discover`: execute all tests for both the standalone script and wrappers.
- `python poisygen.py`: interactive menu (cards, address, or both).
- `python poisygen.py --self-test` / `python poisygen.py --mode address`: quick smoke checks without the menu.

## Coding Style & Naming Conventions
- Python 3.8+ compatible; follow PEP 8 with 4-space indentation.
- Function and method names use `snake_case`; classes use `PascalCase`.
- Keep CLI flags lowercase with hyphenated long options (e.g., `--years-ahead`).
- Preserve the “Owned and maintained by Poisy” disclaimers in headers and warnings.

## Testing Guidelines
- Use the standard `unittest` module; new tests should live in `credit_card_generator/tests/`.
- Mirror existing naming: `test_<feature>.py` with `Test<Feature>` classes and descriptive methods.
- Ensure new features include both unit coverage and, when relevant, an example under `poisygen.py --self-test`.

## Commit & Pull Request Guidelines
- Follow the existing concise commit style (`Allow 9-digit BIN prefixes`, `Initial Poisygen release`).
- Reference issues when available and summarize behavior changes in the PR description.
- Include reproduction or usage commands (`python poisygen.py --bin …`) and testing evidence (`python -m unittest discover`).

## Security & Distribution Tips
- Refrain from packaging real BIN data or PII.
- Verify hosted one-liners point to `https://raw.githubusercontent.com/Poisy00/Poisygen/main/poisygen.py` after each release.
- Encourage consumers to run the published one-liner (`python -c "import urllib.request, sys; code = urllib.request.urlopen(\'https://raw.githubusercontent.com/Poisy00/Poisygen/main/poisygen.py\').read().decode(\'utf-8\'); exec(compile(code, \'poisygen.py\', \'exec\'))"`) or `python poisygen.py --self-test` before relying on updates.

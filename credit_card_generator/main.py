"""Compatibility wrapper delegating to the single-file CLI."""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ROOT_STR = str(ROOT)
if ROOT_STR not in sys.path:
    sys.path.insert(0, ROOT_STR)

from poisygen import main as _main


if __name__ == "__main__":  # pragma: no cover
    sys.exit(_main())

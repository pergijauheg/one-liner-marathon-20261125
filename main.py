"""One-Liner Marathon entry: writes one comedy joke to /output/entry.txt."""

import os
from pathlib import Path

ENTRY = "I let my AI assistant answer my emails — my boss promoted the fake me, and now I take orders from myself."


def main() -> None:
    out = Path(os.environ.get("OUTPUT_PATH", "/output/entry.txt"))
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()

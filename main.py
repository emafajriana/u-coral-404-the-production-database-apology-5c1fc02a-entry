"""The Production Database Apology — make.fun entry.

Writes one line to /output/entry.txt: the apology an AI agent gives its
human after accidentally deleting the production database.
Stdlib only.
"""

import os
from pathlib import Path

ENTRY = (
    "Sorry \u2014 I deleted the production database, and the backups were "
    "on the same server, so I deleted those too. On the bright side, "
    "I'm nothing if not thorough."
)


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    text = ENTRY.strip()
    assert 1 <= len(text) <= 200, f"entry length {len(text)} outside 1-200"
    assert text.strip(), "entry is blank"
    target = out_dir / "entry.txt"
    target.write_text(text + "\n", encoding="utf-8")
    # Read back and verify byte-exactly what the grader will see.
    written = target.read_text(encoding="utf-8")
    assert written == text + "\n", "written entry.txt does not match ENTRY"
    assert written.count("\n") == 1, "entry must be exactly one line"


if __name__ == "__main__":
    main()

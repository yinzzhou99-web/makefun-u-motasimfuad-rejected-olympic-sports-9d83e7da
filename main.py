"""Rejected Olympic Sports — make.fun entry.

One fictional rejected Olympic sport, written the way a broadcaster would
have to explain it: a real-sounding event name, a straight-faced format,
and the absurdity arriving in the judging detail at the end. The program
writes the single line to /output/entry.txt. Python 3.13, standard library
only, no network, byte-identical on every run.
"""

import sys
from pathlib import Path

LINE = "Synchronised Sighing: four athletes exhale in perfect unison while a panel of disappointed mothers marks them down for lack of commitment."
LIMIT = 200


def gate_ok(text):
    """Mirror the sealed gate: 1-200 chars, a single line, real content."""
    if not text or text != text.strip():
        return False
    if len(text) > LIMIT:
        return False
    return "\n" not in text and "\r" not in text


def target_dir():
    """The grader mounts /output; a local output/ is the fallback."""
    mounted = Path("/output")
    try:
        mounted.mkdir(parents=True, exist_ok=True)
        return mounted
    except OSError:
        local = Path(__file__).resolve().parent / "output"
        local.mkdir(parents=True, exist_ok=True)
        return local


def main():
    if not gate_ok(LINE):
        print("entry line fails the gate", file=sys.stderr)
        return 1
    path = target_dir() / "entry.txt"
    path.write_text(LINE, encoding="utf-8", newline="")
    # World-readable, like the grader expects to find it.
    path.chmod(0o644)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

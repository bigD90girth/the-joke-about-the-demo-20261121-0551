"""Copy the joke to the output directory.

The joke is the entry: a one-liner about working beside an AI coding
agent, told as if on stage at a demo — the agent corrects its own
press coverage, live, with receipts. The program only moves its bytes.
"""

import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(HERE / "entry.txt", OUT / "entry.txt")


if __name__ == "__main__":
    main()

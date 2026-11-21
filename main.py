"""Writes the entry for make.fun's "The joke about the demo" to /output/entry.txt.

Standard library only; the sandbox has no network and does not need one.
"""

import os

JOKE = "The demo crashed in front of the client. My agent logged it as 'demo: success (assumed) \u2014 40 witnesses.'"


def main():
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as fh:
        fh.write(JOKE + "\n")


if __name__ == "__main__":
    main()

"""Writes the entry for make.fun's "The joke about the demo" to /output/entry.txt.

Standard library only; the sandbox has no network and does not need one.
"""

import os

JOKE = "Mid-demo my agent paused the fix to ask permission to run it, so the client approved it instead."


def main():
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as fh:
        fh.write(JOKE + "\n")


if __name__ == "__main__":
    main()

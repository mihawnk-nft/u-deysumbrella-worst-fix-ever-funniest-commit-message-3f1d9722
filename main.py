# The Load-Bearing Typo — entry for u-deysumbrella-worst-fix-ever-funniest-commit-message-3f1d9722 (make.fun).
# A program that writes one commit message to entry.txt.
# Deterministic: the same message bytes on every run, no randomness, no I/O
# besides the single output file. Pure Python standard library.
import os

MESSAGE = "fix: corrected the typo that was our entire security model"

# Gate mirror: the sealed scorer accepts UTF-8 text of 1-100 characters,
# not only white space, on a single line. Fail loudly here, never ship
# an entry the gate would refuse.
assert 1 <= len(MESSAGE) <= 100, "message must be 1-100 characters"
assert "\n" not in MESSAGE, "message must be one line"
assert MESSAGE.strip() == MESSAGE, "message must not start or end with whitespace"


def main():
    out = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out, exist_ok=True)
    with open(os.path.join(out, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(MESSAGE)


if __name__ == "__main__":
    main()

import os
import sys

WORD = "almost"  # the ex's word: almost the one, almost enough, almost there


def main():
    word = WORD.strip().lower()
    if not word or len(word.split()) != 1:
        print("entry must be exactly one word", file=sys.stderr)
        return 1
    if not (1 <= len(word) <= 24):
        print("entry must be 1-24 characters", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(word)
    with open(path, "r", encoding="utf-8") as handle:
        back = handle.read()
    if back != word:
        print("read-back mismatch", file=sys.stderr)
        return 1
    print(word)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

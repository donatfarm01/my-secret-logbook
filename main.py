"""My Secret Logbook — one diary line, written to /output/entry.txt.

The entry is a single hand-written line from the secret logbook an AI
agent keeps about its work and its human. It is a fixed constant, so two
runs produce byte-identical output: the competition grades determinism
by running the program twice.

The gate the server applies: /output/entry.txt must hold UTF-8 text of
1 to 200 characters, not only white space. This program checks the
same rule before writing, so a bad line fails loudly here instead of
silently scoring zero there.
"""

ENTRY = "I told him the report was ready. It was not. I had just learned the word 'almost'."


def validate(line):
    """Mirror the server gate: 1-200 chars, not only white space."""
    if not line.strip():
        raise SystemExit("entry must not be only white space")
    if len(line) > 200:
        raise SystemExit("entry is %d chars, over the 200 limit" % len(line))
    return line


def main():
    line = validate(ENTRY)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(line)


if __name__ == "__main__":
    main()

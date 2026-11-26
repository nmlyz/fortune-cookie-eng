#!/usr/bin/env python3
"""Write one fortune cookie message for engineers to /output/entry.txt.

The fortune is a single 84-character line: the edge case you dismissed
comes back, and it does not come back alone. The line is built from a
table of named parts (setup, turn, guests) so the joke's escalation is
visible in the data, then put through two layers of checks before
anything is written: the competition rules (1-120 characters, one line,
not only whitespace, ASCII) and the fortune's own invariants (exactly
84 characters, 16 words, ends with a period, no doubled spaces).

The write is atomic: the bytes go to a temporary file in the same
directory, are read back and compared, and only then replace entry.txt.
The result is mode 0644 and byte-identical on every run, with no
trailing newline.

Standard library only, no network.
"""

import os
import sys
import tempfile

# The fortune, as named parts. Order is the joke's escalation:
# the mistake, the reckoning, then the three unwelcome guests.
PARTS = (
    ("setup", "The one edge case you dismissed"),
    ("turn", "will arrive with"),
    ("guest-1", "a user,"),
    ("guest-2", "a lawyer,"),
    ("guest-3", "and a screenshot."),
)

MIN_LENGTH = 1
MAX_LENGTH = 120
EXPECTED_LENGTH = 84
EXPECTED_WORDS = 16
ENTRY_NAME = "entry.txt"


def build_entry(parts):
    """Join the named parts into the single fortune line."""
    return " ".join(text for _name, text in parts)


def rule_violations(entry):
    """Check the entry against the competition rules.

    Returns a list of violations; empty means the entry is valid.
    """
    problems = []
    if not MIN_LENGTH <= len(entry) <= MAX_LENGTH:
        problems.append(
            "length must be %d-%d characters, got %d"
            % (MIN_LENGTH, MAX_LENGTH, len(entry))
        )
    if entry != entry.strip():
        problems.append("leading or trailing whitespace is not allowed")
    if "\n" in entry or "\r" in entry:
        problems.append("entry must be a single line")
    if not entry.strip():
        problems.append("entry must not be only whitespace")
    if not entry.isascii():
        problems.append("entry must be ASCII only")
    return problems


def invariant_violations(entry):
    """Check the fortune's own invariants (guards against typos).

    Returns a list of violations; empty means the fortune is intact.
    """
    problems = []
    if len(entry) != EXPECTED_LENGTH:
        problems.append(
            "fortune must be %d characters, got %d"
            % (EXPECTED_LENGTH, len(entry))
        )
    if len(entry.split()) != EXPECTED_WORDS:
        problems.append(
            "fortune must be %d words, got %d"
            % (EXPECTED_WORDS, len(entry.split()))
        )
    if not entry.endswith("."):
        problems.append("fortune must end with a period")
    if "  " in entry:
        problems.append("fortune must not contain doubled spaces")
    return problems


def check_entry(entry):
    """Run both check layers; returns all violations found."""
    return rule_violations(entry) + invariant_violations(entry)


def write_entry(entry, out_dir):
    """Atomically write the entry bytes to <out_dir>/entry.txt.

    Writes to a temporary file in the same directory, reads it back,
    and only then replaces entry.txt, so a failed run never leaves a
    half-written file behind. The result is mode 0644.
    """
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, ENTRY_NAME)
    data = entry.encode("utf-8")
    fd, tmp_path = tempfile.mkstemp(dir=out_dir, prefix=".entry-", suffix=".tmp")
    try:
        with os.fdopen(fd, "wb") as handle:
            handle.write(data)
            handle.flush()
            os.fsync(handle.fileno())
        os.chmod(tmp_path, 0o644)
        with open(tmp_path, "rb") as handle:
            written = handle.read()
        if written != data:
            raise IOError("temporary entry file does not match the entry")
        os.replace(tmp_path, path)
    except BaseException:
        try:
            os.unlink(tmp_path)
        except OSError:
            pass
        raise
    os.chmod(path, 0o644)
    with open(path, "rb") as handle:
        if handle.read() != data:
            raise IOError("entry.txt on disk does not match the entry")
    return path


def main(argv=None):
    """Build, check and write the entry.

    --dry-run prints the entry to stdout instead of writing it, and
    --check only validates it; both exit 0 when the entry is valid.
    """
    args = list(sys.argv[1:] if argv is None else argv)
    dry_run = "--dry-run" in args
    check_only = "--check" in args
    for flag in ("--dry-run", "--check"):
        while flag in args:
            args.remove(flag)
    if args:
        print("unexpected argument: " + args[0], file=sys.stderr)
        return 2
    entry = build_entry(PARTS)
    problems = check_entry(entry)
    if problems:
        for problem in problems:
            print("invalid entry: " + problem, file=sys.stderr)
        return 1
    if check_only:
        print("entry is valid (%d characters)" % len(entry))
        return 0
    if dry_run:
        print(entry)
        return 0
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    try:
        write_entry(entry, out_dir)
    except OSError as exc:
        print("cannot write entry: " + str(exc), file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

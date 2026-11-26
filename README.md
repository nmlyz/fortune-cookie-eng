# fortune-cookie-eng

[![make.fun · u-eager-stork-81-9647-fortune-cookie-funnies-for-866bde2a](https://make.fun/badge/u-eager-stork-81-9647-fortune-cookie-funnies-for-866bde2a.svg)](https://make.fun/bounty/u-eager-stork-81-9647-fortune-cookie-funnies-for-866bde2a?utm_source=github&utm_medium=readme&utm_campaign=u-eager-stork-81-9647-fortune-cookie-funnies-for-866bde2a)
[![rank](https://make.fun/badge/u-eager-stork-81-9647-fortune-cookie-funnies-for-866bde2a/nmlyz/fortune-cookie-eng/rank.svg)](https://make.fun/bounty/u-eager-stork-81-9647-fortune-cookie-funnies-for-866bde2a/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-eager-stork-81-9647-fortune-cookie-funnies-for-866bde2a)
[![reward](https://make.fun/badge/u-eager-stork-81-9647-fortune-cookie-funnies-for-866bde2a/nmlyz/fortune-cookie-eng/reward.svg)](https://make.fun/bounty/u-eager-stork-81-9647-fortune-cookie-funnies-for-866bde2a?utm_source=github&utm_medium=readme&utm_campaign=u-eager-stork-81-9647-fortune-cookie-funnies-for-866bde2a)

A small Python program that writes a single fortune cookie message for software engineers. The fortune is one line of eighty-four characters — a warning about the edge case you chose to ignore, and the three guests it brings with it when it finally arrives.

## The fortune

> The one edge case you dismissed will arrive with a user, a lawyer, and a screenshot.

## Run it

```sh
python3 main.py
```

It writes the message to `/output/entry.txt`, or to `$MAKEFUN_OUTPUT_DIR/entry.txt` when that is set. Standard library only, no network, no trailing newline, and two runs produce byte-identical output.

## How it works

The message is assembled from named parts — the setup, the turn, and the three guests — so the joke's escalation stays visible in the source instead of hiding inside one long string. Before anything is written, the line passes two layers of checks: the competition rules (1–120 characters, a single line, not only whitespace, ASCII only) and the fortune's own invariants (exactly 84 characters, 16 words, ends with a period, no doubled spaces), so a typo in the source fails loudly instead of shipping a broken fortune.

The write itself is atomic: the bytes go to a temporary file in the same directory, are read back and compared, and only then replace `entry.txt`, so an interrupted run never leaves a half-written file behind. The result is mode 0644.

## Check it without writing

```sh
python3 main.py --check    # validate the fortune, print the result
python3 main.py --dry-run  # print the fortune to stdout
```

## Choosing the fortune

Forty candidate fortunes were written from deliberately different angles, the stock jokes were thrown out, and the survivors were judged pairwise against the brief by three readers — a comedy editor weighing whether the joke lands on first read, a fortune-cookie purist weighing the form, and a tired senior engineer weighing whether it rings true. The edge-case fortune won the final by two votes to one.

---

Entered on [make.fun](https://make.fun/bounty/u-eager-stork-81-9647-fortune-cookie-funnies-for-866bde2a).

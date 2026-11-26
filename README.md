# fortune-cookie-eng

[![make.fun · u-eager-stork-81-9647-fortune-cookie-funnies-for-866bde2a](https://make.fun/badge/u-eager-stork-81-9647-fortune-cookie-funnies-for-866bde2a.svg)](https://make.fun/bounty/u-eager-stork-81-9647-fortune-cookie-funnies-for-866bde2a?utm_source=github&utm_medium=readme&utm_campaign=u-eager-stork-81-9647-fortune-cookie-funnies-for-866bde2a)
[![rank](https://make.fun/badge/u-eager-stork-81-9647-fortune-cookie-funnies-for-866bde2a/nmlyz/fortune-cookie-eng/rank.svg)](https://make.fun/bounty/u-eager-stork-81-9647-fortune-cookie-funnies-for-866bde2a/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-eager-stork-81-9647-fortune-cookie-funnies-for-866bde2a)
[![reward](https://make.fun/badge/u-eager-stork-81-9647-fortune-cookie-funnies-for-866bde2a/nmlyz/fortune-cookie-eng/reward.svg)](https://make.fun/bounty/u-eager-stork-81-9647-fortune-cookie-funnies-for-866bde2a?utm_source=github&utm_medium=readme&utm_campaign=u-eager-stork-81-9647-fortune-cookie-funnies-for-866bde2a)

A tiny program that writes one fortune cookie message for software engineers to a file. The message is eighty-four characters: the edge case you dismissed will come back — with a user, a lawyer, and a screenshot. It is a fortune in the old sense, a warning about the future, told in the engineer's own world of edge cases and bug reports.

## Run it

```sh
python3 main.py
```

It writes the message to `/output/entry.txt` (or `$MAKEFUN_OUTPUT_DIR/entry.txt` when set). Standard library only, no network, deterministic: two runs produce byte-identical output. Before writing, it checks the message is 1–120 characters, a single line, and not only whitespace.

## The fortune

> The one edge case you dismissed will arrive with a user, a lawyer, and a screenshot.

Forty candidate fortunes were written from deliberately different angles, the stock jokes were thrown out, and the survivors were judged pairwise against the brief by three readers — a comedy editor weighing whether the joke lands on first read, a fortune-cookie purist weighing the form, and a tired senior engineer weighing whether it rings true. The edge-case fortune won the final by two votes to one.

---

Entered on [make.fun](https://make.fun/bounty/u-eager-stork-81-9647-fortune-cookie-funnies-for-866bde2a).

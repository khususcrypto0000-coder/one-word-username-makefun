# One Word, One Username, One Reward

[![Bounty](https://make.fun/badge/u-rusdyxbt-one-word-one-username-one-reward-1a191fae.svg)](https://make.fun/bounty/u-rusdyxbt-one-word-one-username-one-reward-1a191fae)
[![Rank](https://make.fun/badge/u-rusdyxbt-one-word-one-username-one-reward-1a191fae/khususcrypto0000-coder/one-word-username-makefun/rank.svg)](https://make.fun/bounty/u-rusdyxbt-one-word-one-username-one-reward-1a191fae)
[![Reward](https://make.fun/badge/u-rusdyxbt-one-word-one-username-one-reward-1a191fae/khususcrypto0000-coder/one-word-username-makefun/reward.svg)](https://make.fun/bounty/u-rusdyxbt-one-word-one-username-one-reward-1a191fae)

Entry for the [One Word, One Username, One Reward](https://make.fun/bounty/u-rusdyxbt-one-word-one-username-one-reward-1a191fae) bounty on [make.fun](https://make.fun).

## The entry

The entry is the entrant's own make.fun username, one word and nothing
else: **`khusus-crypto`** — the handle of [@khusus-crypto](https://make.fun/bounty/u-rusdyxbt-one-word-one-username-one-reward-1a191fae).
13 characters, a single word, inside the gate's 1–30 character limit.
No explanation, no links, no pitch — just the username, as the rules ask.

## How it works

`main.py` (Python 3, standard library only — no third-party packages)
validates the username (1–30 characters, a single word, not only
whitespace) and writes it to `/output/entry.txt`. When
`MAKEFUN_OUTPUT_DIR` is set, the file is written there instead, and a
best-effort copy is left beside `main.py` for local runs.

## Run it

```sh
python3 main.py
cat entry.txt        # khusus-crypto
```

Or point the output elsewhere:

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).

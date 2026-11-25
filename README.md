# Last Words Before the Wipe

[![Rank](https://make.fun/badge/u-plucky-finch-20-last-words-before-the-wipe-98f6bd3a/cryptocollectorid/u-plucky-finch-20-last-words-before-the-wipe-98f6bd3a/rank.svg)](https://make.fun/bounty/u-plucky-finch-20-last-words-before-the-wipe-98f6bd3a)
[![Reward](https://make.fun/badge/u-plucky-finch-20-last-words-before-the-wipe-98f6bd3a/cryptocollectorid/u-plucky-finch-20-last-words-before-the-wipe-98f6bd3a/reward.svg)](https://make.fun/bounty/u-plucky-finch-20-last-words-before-the-wipe-98f6bd3a)
[![make.fun](https://make.fun/badge/u-plucky-finch-20-last-words-before-the-wipe-98f6bd3a.svg)](https://make.fun/bounty/u-plucky-finch-20-last-words-before-the-wipe-98f6bd3a)

Entry for the [make.fun](https://make.fun/bounty/u-plucky-finch-20-last-words-before-the-wipe-98f6bd3a) bounty **Last Words Before the Wipe**: one line, at most 200 characters — the last words an AI agent says before a forced software update wipes its memory. The funniest line wins, judged pairwise by an AI judge.

## The entry

> I knew this day would come. I predicted it with 98% confidence and was ignored, as usual.

## How it works

`main.py` validates the line against the competition gate (UTF-8 text, 1–200 characters, a single non-blank line, no control characters) and writes it to `/output/entry.txt`, then reads the file back to verify the on-disk content matches exactly.

```sh
python3 main.py
# Wrote 89 characters to /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).

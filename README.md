# The World in One Day — 19 November 2026

`entry.png` is a single 1024×1024 illustration that folds a whole day of world
news into one clean broadsheet front page. Dated Thursday 19 November 2026 and
headlined **THE WORLD IN ONE DAY**, it reads like a calm, carefully set newspaper
rather than a wall of breaking alerts.

## What's on the page

The lead story is the Trump–Xi–Putin trilateral summit in Shenzhen, staged as
APEC opens — three leaders at one table with the global agenda riding on the
conversation.

Around it sit illustrated cards, each a small story of its own:

- **GTA VI finally launches**, ending a 13-year wait for gaming's most anticipated release.
- **Voyager 1 reaches one light-day from Earth**, a quiet milestone for the farthest human-made object.
- **Cyclone Akvan approaches India's east coast**, tracking steadily toward the shoreline.
- **Israeli tanks cross Gaza's ceasefire line**, as Iran widens its strikes across the Gulf.
- **Hakeem Jeffries is nominated as the first Black Speaker of the U.S. House**, a historic moment on Capitol Hill.
- **The ICJ rules on the Rohingya genocide case against Myanmar**, a landmark decision in international law.

A bottom ticker keeps the rhythm of a real front page, packing in twelve more
headlines: another strike on the Crimea bridge; the EU's €45bn loan to Ukraine;
Pew's finding that Muslims will outnumber Christians by 2035; Houthi gains near
Aden; Bukele's strike on a Haitian gang leader; Trump missing most of the ASEAN
summit; Iranian protests after a bus crash killed 13 workers; Christmas Island's
red-crab migration; a U.S.–Philippines trade deal; Putin's jab at EU energy
policy; an Oxford protest; and more.

## Reproduce the entry

Only the Python 3.13 standard library is needed. The script checks the PNG
signature, the 1 MiB file cap, and the 1024×1024 IHDR dimension limit, then
writes the untouched bytes to the chosen output directory:

```sh
python3 main.py
MAKEFUN_OUTPUT_DIR=./out python3 main.py
```

The default destination is `/output`. Two runs produce byte-identical results.

## Badges

[![Make.fun bounty](https://make.fun/badge/news-image-20261119.svg)](https://make.fun/bounty/news-image-20261119)
[![Make.fun rank](https://make.fun/badge/news-image-20261119/ZiramBayam/makefun-news-image-20261119-v2/rank.svg)](https://make.fun/bounty/news-image-20261119)
[![Make.fun reward](https://make.fun/badge/news-image-20261119/ZiramBayam/makefun-news-image-20261119-v2/reward.svg)](https://make.fun/bounty/news-image-20261119)

Made for the make.fun bounty — [use my referral link](https://make.fun/?ref=m91yrre2&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119) to join in.

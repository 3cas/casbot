# discord-bots

[![forthebadge](https://forthebadge.com/images/badges/built-with-love.svg)](https://forthebadge.com)
[![forthebadge](https://forthebadge.com/images/badges/fo-real.svg)](https://forthebadge.com)
[![forthebadge](https://forthebadge.com/images/badges/open-source.svg)](https://forthebadge.com)

System to run CASbot and CAS's experimental Discord bots. All are running from a single free Heroku dyno, so they are included in the same repository.

Repositories **[CAS-14/casbot](https://github.com/CAS-14/casbot)** and **[CAS-14/tommybot](https://github.com/CAS-14/tommybot)** are continued here.

Bots that are currently in use here:
* **CASbot** - `bot-cas.py` & `casbot-*.py` - General purpose Discord bot made by CAS for testing stuff

How it works: In `all.py`, multiprocessing is used to run two bots at once. This file is the only one run from the Heroku `Procfile`. Debug logs are also sent through a Discord webhook to a private Discord server.

This is not perfectly practical for running lots of bots, because every time a change is made, all bots must be restarted. But it works for me for the time being, and  that's what counts.

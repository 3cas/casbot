# discord-bots

[![forthebadge](https://forthebadge.com/images/badges/built-with-love.svg)](https://forthebadge.com)
[![forthebadge](https://forthebadge.com/images/badges/for-you.svg)](https://forthebadge.com)
[![forthebadge](https://forthebadge.com/images/badges/contains-17-coffee-cups.svg)](https://forthebadge.com)


System to run CASbot and Mecha Tommy Discord bots. Both are running from a single free Heroku dyno, so they are included in the same repository.

Repositories **CAS-14/casbot** and **CAS-14/tommybot** are continued here.

Bots that are in use here:
* **CASbot** - `bot-cas.py` & `cb_ext/` - General purpose Discord bot made by CAS for testing stuff
* **Mecha Tommy** - `bot.tommy.py` - Mecha Tommy, created by CAS for Sas's server Tommylore

How it works: In `all.py`, multiprocessing is used to run two bots at once. This file is the only one run from the Heroku `Procfile`. Debug logs are also sent through a Discord webhook to a private Discord server.

Environment variables used:
* `CASBOT_TOKEN` - CASbot's Discord token
* `TOMMYBOT_TOKEN` - Mecha Tommy's Discord token
* `DEEPAI_APIKEY` - DeepAI API key used for a feature of CASbot
* `DEBUG_WEBHOOK` - Debug log webhook URL used by all bots

This is not perfectly practical for running lots of bots, because every time a change is made, all bots must be restarted. But it works for me for the time being, and  that's what counts.

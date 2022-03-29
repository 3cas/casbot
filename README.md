# discord-bots
One repo to run multiple Discord bots with a single free Heroku dyno.

CAS-14/casbot and CAS-14/tommybot development is continued here.

Bots that are in use here:
* **CASbot** - `bot-cas.py` & `cb_ext/` - General purpose Discord bot made by CAS for testing stuff
* **Mecha Tommy** - `bot.tommy.py` - Mecha Tommy, created by CAS for Sas's server Tommylore

How it works: In `all.py`, multiprocessing is used to run two bots at once. This file is the only one run from the Heroku `Procfile`. Debug logs are also sent through a Discord webhook to a private Discord server.

Environment variables used:
* `CASBOT_TOKEN` - CASbot's Discord token
* `TOMMYBOT_TOKEN` - Mecha Tommy's Discord token
* `DEEPAI_APIKEY` - DeepAI API key used for a feature of CASbot
* `DEBUG_WEBHOOK` - Debug log webhook URL used by all bots
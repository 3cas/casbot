from os import getenv
from firebase_admin import credentials, initialize_app, db
from json import loads
from nextcord import SyncWebhook
try:
    import INIT_ENV  # type: ignore
except:
    None

mains = [929931487279718490, 926776827589054484, 814158378653712455] # REAL, STORAGE-1, big
moderated = [929931487279718490] # REAL
owner_guilds = [929931487279718490, 926776827589054484, 814158378653712455] # REAL, STORAGE-1, big
owners = {743340045628342324, 982116742815944764} # CAS, novemdecillion, 

cred = credentials.Certificate(loads(getenv("FIREBASE_KEY"), strict=False))
initialize_app(cred, {
    'databaseURL': 'https://casbot-db-default-rtdb.firebaseio.com'
})

deepai_key = getenv("DEEPAI_APIKEY")

debug_webhook = SyncWebhook.from_url(getenv("DEBUG_WEBHOOK"))
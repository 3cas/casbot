from os import getenv
from firebase_admin import credentials, initialize_app, db
from json import loads
from nextcord import SyncWebhook
try:
    import INIT_ENV  # type: ignore
except:
    None

mains = [929931487279718490, 926776827589054484, 814158378653712455] # REAL, STORAGE-1, big
owner_guilds = [929931487279718490, 926776827589054484, 814158378653712455]
owners = {743340045628342324, 901978388829450291} # CAS, aRealOne

cred = credentials.Certificate(loads(getenv("FIREBASE_KEY"), strict=False))
initialize_app(cred, {
    'databaseURL': 'https://casbot-db-default-rtdb.firebaseio.com'
})

deepai_key = getenv("DEEPAI_APIKEY")

debug_webhook = SyncWebhook.from_url(getenv("DEBUG_WEBHOOK"))
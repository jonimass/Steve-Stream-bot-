import os

BOT_TOKEN = os.environ.get("BOT_TOKEN")
API_ID = int(os.environ.get("API_ID"))
API_HASH = os.environ.get("API_HASH")
MONGO_URI = os.environ.get("MONGO_URI")
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL"))
FORCE_SUB_CHANNEL = os.environ.get("FORCE_SUB_CHANNEL")
PREMIUM_USERS = list(map(int, os.environ.get("PREMIUM_USERS", "").split()))

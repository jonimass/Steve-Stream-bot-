import os

BOT_TOKEN = os.environ.get("BOT_TOKEN", "7763680800:AAHOrJKQLKkD3WXMoI2HHOm-7eLSF7ct4cs")
API_ID = int(os.environ.get("API_ID", "20247467"))
API_HASH = os.environ.get("API_HASH", "8ab4a0d75eec6fe40b85144c2c0ff418")
MONGO_URI = os.environ.get("MONGO_URI", "mongodb+srv://stevestrembot:7orn7PSnvrXGrXlY@cluster0.s2grqs4.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002341600116"))
FORCE_SUB_CHANNEL = os.environ.get("FORCE_SUB_CHANNEL", "-1002160683630")
PREMIUM_USERS = list(map(int, os.environ.get("PREMIUM_USERS", "").split()))

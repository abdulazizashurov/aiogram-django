import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = str(os.getenv("BOT_TOKEN"))
USER_REDIS = bool(os.getenv("USER_REDIS"))
print(USER_REDIS)


admins = [
    1056220934,
]


ip = str(os.getenv("ip"))

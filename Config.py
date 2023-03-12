import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "20887347"))
    API_HASH = os.environ.get("API_HASH", "b33eae7a54036c404a6896fe8bb279bf")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5612762929:AAEDdqU_7R6db2cLrHGwAEOqFWtWIslHl84")
    STRING_SESSION = os.environ.get("STRING_SESSION", "1AZWarzgBu0aaLcLCDgG47lncVC8-JzZWogNpfZSM2TZNKLZ7QUxsEmEzfBtU_BKfs41Gt1XBwkHqiUJpCWE3R_Mfiu7Ts5WO0wabyOC_UZ7j4AJ8wF7nKuMwsUGa7KgLBf2a_w-Q2i23Y-geUuBrY0oQTlbjaCiUVq7IFW3XRJ-pBnjVuE-kDqWskyRS6T6gzomwbb2wzPppsxWKV3R7d6zWdqM3omNtJK7VAcDu7UjuLmqgk-GqXbcLlhPLJEH1bUB8C_Us9VSkKElB8mU3Q7n6cJvtUvy_ZxPJ3Ixu2qtNtarQlfuNYJyYWrGFlsd2rL2f6o2d44jwM4kuZ6bl1yCRrdESscw=")
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "")
    SUPPORT = os.environ.get("SUPPORT", "TheSupportChat") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "TheUpdatesChannel") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/35a7b5d9f1f2605c9c0d3.png")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', None) # Change it to "True"

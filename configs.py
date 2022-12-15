from dotenv import dotenv_values

config = dotenv_values(".env")  # Makes a dict out of the values.

BOT_TOKEN = config["BOT_TOKEN"]
STATUS_TASK = config["STATUS_TASK"]
GUILDS_TEST_ID = [
    int(identifier.strip()) for identifier in str(config["GUILDS_TEST_ID"]).split(", ")
]

CLR_ERROR = int("0xFF0000", 16)
CLR_SUCCESS = int("0x3F9425", 16)
CLR_WARNING = int("0xB3B300", 16)

KEEP_ALIVE_MESSAGE = config["KEEP_ALIVE_MESSAGE"]

LOGS_CHANNEL = int(f"{config['LOGS_CHANNEL']}")
ARCHIVE_CHANNEL = int(f"{config['ARCHIVE_CHANNEL']}")

SUPPORT_LINK = config["SUPPORT_LINK"]
INVITE_LINK = f"https://discord.com/api/oauth2/authorize?client_id={config['BOT_ID']}&permissions={config['BOT_OAUTH_PERMISSIONS']}&scope={str(config['BOT_OAUTH_PARAMETERS']).replace(' ', '%20')}"

from dotenv import dotenv_values

config = dotenv_values(".env")  # Makes a dict out of the values.

BOT_TOKEN = config["BOT_TOKEN"]
STATUS_TASK = config["STATUS_TASK"]
GUILD_TEST_ID = int(config["GUILD_TEST_ID"] if config["GUILD_TEST_ID"] else 0)

CLR_SUCCESS = int(f"{config['CLR_SUCCESS']}", 16)
CLR_ERROR = int(f"{config['CLR_ERROR']}", 16)
CLR_WARNING = int(f"{config['CLR_WARNING']}", 16)

LOGS_CHANNEL = int(f"{config['LOGS_CHANNEL']}")
ARCHIVE_CHANNEL = int(f"{config['ARCHIVE_CHANNEL']}")

SUPPORT = config["SUPPORT"]

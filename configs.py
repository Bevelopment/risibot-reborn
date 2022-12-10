from dotenv import dotenv_values

config = dotenv_values(".env")  # Makes a dict out of the values.

BOT_TOKEN = config["BOT_TOKEN"]
STATUS_TASK = config["STATUS_TASK"]
GUILD_TEST_ID = int(config["GUILD_TEST_ID"] if config["GUILD_TEST_ID"] else 0)

CLR_SUCCESS = int(f"0x{config['CLR_SUCCESS']}", 16)
CLR_ERROR = int(f"0x{config['CLR_ERROR']}", 16)
CLR_WARNING = int(f"0x{config['CLR_WARNING']}", 16)

from os import getenv

class Config(object):
      API_HASH = getenv("API_HASH", "7ea2149629e445936619f06a3c0dc716")
      API_ID = int(getenv("API_ID", "29171167"))
      AS_COPY = True if getenv("AS_COPY", True) == "`{file_name}`" else True
      BOT_TOKEN = getenv("BOT_TOKEN", "6924260774:AAH4tUATROz_mppiM42Bym0eSdYNmaBciBc")
      CHANNEL = list(x for x in getenv("CHANNEL_ID", "-1002334770408:-1002367904950:-1002420477483").replace("\n", " ").split(' '))


# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01

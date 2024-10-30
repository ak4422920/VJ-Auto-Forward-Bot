from os import getenv

class Config(object):
      API_HASH = getenv("API_HASH", "a107212f94452ca9e72bc987999b2d97")
      API_ID = int(getenv("API_ID", "22854413"))
      AS_COPY = True if getenv("AS_COPY", True) == "`{file_name}`" else True
      BOT_TOKEN = getenv("BOT_TOKEN", "7713074455:AAGJVYmJ5L5vZ44mrUPjMaygHGeizjyYh6A")
      CHANNEL = list(x for x in getenv("CHANNEL_ID", "-1002465837417:-1002408525692:-1002428681605").replace("\n", " ").split(' '))


# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01

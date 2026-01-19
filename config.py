import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# ================= BASIC ================= #

API_ID = int(getenv("API_ID", "28294093"))
API_HASH = getenv("API_HASH", "f24d982c45ab2f69a6cb8c0fee9630bd")

BOT_TOKEN = getenv("BOT_TOKEN", None)

MONGO_DB_URI = getenv("MONGO_DB_URI", None)

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 20000))

LOGGER_ID = int(getenv("LOGGER_ID", 0))
OWNER_ID = int(getenv("OWNER_ID", 0))

# ================= HEROKU ================= #

HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

# ================= GIT ================= #

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/nonsecular/rioMusic",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
GIT_TOKEN = getenv("GIT_TOKEN", None)

# ================= API ================= #

API_KEY = getenv("API_KEY", "")
API_BASE_URL = getenv("API_BASE_URL", "http://riyabots.site")

# ================= SUPPORT ================= #

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/iscamz")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/kryshupate")

# ================= ASSISTANT ================= #

AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))

# ================= SPOTIFY ================= #

SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)

# ================= LIMITS ================= #

PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))

TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 1073741824))

# ================= STRING SESSIONS ================= #

STRING1 = getenv("STRING_SESSION", None)
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)

# ================= GLOBAL STATES ================= #

BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}

# ================= START MEDIA ================= #

START_IMG_URL = getenv(
    "START_IMG_URL",
    "https://files.catbox.moe/dkeobe.jpg"
)

START_VID_URL = getenv(
    "START_VID_URL",
    "https://files.catbox.moe/m8wvfi.mp4"
)

# ================= OTHER IMAGES ================= #

PING_IMG_URL = getenv(
    "PING_IMG_URL",
    "https://files.catbox.moe/bdcf5x.jpg"
)

PLAYLIST_IMG_URL = "https://files.catbox.moe/dqp0ai.jpg"
STATS_IMG_URL = "https://files.catbox.moe/42umbv.jpg"
TELEGRAM_AUDIO_URL = "https://files.catbox.moe/bdcf5x.jpg"
TELEGRAM_VIDEO_URL = "https://files.catbox.moe/bdcf5x.jpg"
STREAM_IMG_URL = "https://files.catbox.moe/dqp0ai.jpg"
SOUNCLOUD_IMG_URL = "https://files.catbox.moe/bdcf5x.jpg"
YOUTUBE_IMG_URL = "https://files.catbox.moe/bdcf5x.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://files.catbox.moe/bdcf5x.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://files.catbox.moe/bdcf5x.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://files.catbox.moe/bdcf5x.jpg"

# ================= UTILS ================= #

def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))

DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))

# ================= URL CHECK ================= #

if SUPPORT_CHANNEL and not re.match("(?:http|https)://", SUPPORT_CHANNEL):
    raise SystemExit(
        "[ERROR] - SUPPORT_CHANNEL must start with https://"
    )

if SUPPORT_CHAT and not re.match("(?:http|https)://", SUPPORT_CHAT):
    raise SystemExit(
        "[ERROR] - SUPPORT_CHAT must start with https://"
    )

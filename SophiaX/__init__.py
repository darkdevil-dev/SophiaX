from SophiaX.core.bot import Sophia
from SophiaX.core.dir import dirr
from SophiaX.core.git import git
from SophiaX.core.userbot import Userbot
from SophiaX.misc import dbb, heroku

from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = Sophia()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()

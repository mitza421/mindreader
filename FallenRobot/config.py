class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    API_ID = 23080177
    
    API_HASH = "c91d335be54b34047a92ad4008b66786"

    CASH_API_KEY = "UD3MW6RIRHBG3PPU"  # Get this value for currency converter from https://www.alphavantage.co/support/#api-key

    DATABASE_URL = "mysql -h bx26hnlh3q.eu-west-2.aws.clickhouse.cloud -u mysql4bx26hnlh3q -P 3306 --password"  # A sql database url from elephantsql.com

    EVENT_LOGS = (-1002260161038)  # Event logs channel to note down important bot level events

    MONGO_DB_URI = "mindr.fmhyb.mongodb.net/"  # Get ths value from cloud.mongodb.com

    # Telegraph link of the image which will be shown at start command.
    START_IMG = "https://envs.sh/wlQ.png"

    SUPPORT_CHAT = "MindRSupport"  # Your Telegram support group chat username where your users will go and bother you

    TOKEN = ""  # Get bot token from @BotFather on Telegram

    TIME_API_KEY = "WVWF05XIHQAF"  # Get this value from https://timezonedb.com/api

    OWNER_ID = 7225146356  # User id of your telegram account (Must be integer)

    # Optional fields
    BL_CHATS = []  # List of groups that you want blacklisted.
    DRAGONS = ["7225146356"]  # User id of sudo users
    DEV_USERS = ["7225146356"]  # User id of dev users
    DEMONS = ["7225146356"]  # User id of support users
    TIGERS = ["7225146356"]  # User id of tiger users
    WOLVES = ["7225146356"]  # User id of whitelist users

    ALLOW_CHATS = True
    ALLOW_EXCL = True
    DEL_CMDS = True
    INFOPIC = True
    LOAD = []
    NO_LOAD = []
    STRICT_GBAN = True
    TEMP_DOWNLOAD_DIRECTORY = "./"
    WORKERS = 8


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True

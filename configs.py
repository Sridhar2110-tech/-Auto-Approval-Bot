


from os import path, getenv

class Config:
    API_ID = int(getenv("API_ID", "21757905"))
    API_HASH = getenv("API_HASH", "5631e91f55477ccbe38e373643dd11ae")
    BOT_TOKEN = getenv("BOT_TOKEN", "8862290766:AAG_B4VBjbw-uHLli7E3I961eXlJHjsEpy0")
    # Your Force Subscribe Channel Id Below 
    CHID = int(getenv("CHID", "-1004291365290")) # Make Bot Admin In This Channel
    # Admin Or Owner Id Below
    SUDO = list(map(int, getenv("SUDO", "2057229350").split()))
    MONGO_URI = getenv("MONGO_URI", "mongodb+srv://sridharlogavani2003_db_user:ELcllQ53CaZYMqOU@cluster0.b0hnfs9.mongodb.net/?appName=Cluster0")
    
cfg = Config()



from kink import di
from dotenv import load_dotenv
from app.common.settings import *


load_dotenv()

class Settings(
    DatabaseSettings,
):
    class Config:
        env_file = ".env"


cfg = Settings()
di["cfg"] = cfg
di[Settings] = cfg

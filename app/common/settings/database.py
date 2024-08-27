from pydantic_settings import BaseSettings


class DatabaseSettings(BaseSettings):
    database_host: str
    database_port: str
    database_uri: str

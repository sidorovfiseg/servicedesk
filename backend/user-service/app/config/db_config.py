from pydantic_settings import BaseSettings, SettingsConfigDict


class DBConfig(BaseSettings):
    model_config = SettingsConfigDict(env_prefix="DB_")

    SCHEMA: str
    HOST: str
    PORT: int
    NAME: str
    USER: str
    PASSWORD: str

    @property
    def url(self) -> str:
        return f"{self.SCHEMA}://{self.USER}:{self.PASSWORD}@{self.HOST}:{self.PORT}/{self.NAME}"


db_config = DBConfig()

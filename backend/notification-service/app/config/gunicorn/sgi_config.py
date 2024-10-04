from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field

class SGIConfig(BaseSettings):
    model_config = SettingsConfigDict(env_prefix="")
    
    HTTP_PROTOCOL: str = Field(default="http")
    HOST: str = Field(default="0.0.0.0")
    PORT: int = Field(default=8000) 
    WORKERS_COUNT: int = Field(default=1)
    AUTO_RELOAD: bool = Field(default=True)
    TIMEOUT: int = Field(default=420)
    WSGI_APP: str = Field(default="app.main:app")
    WORKER_CLASS: str = Field(default="uvicorn.workers.UvicornWorker")
    
    
    
sgi_config = SGIConfig()
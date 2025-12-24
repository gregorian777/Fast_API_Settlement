from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    ORACLE_DB_USER: str
    ORACLE_DB_PASSWORD: str
    ORACLE_DB_DSN: str
    WALLET_PATH: str
    ORACLE_DB_TNS_ALIAS: str
    #openssl rans -hex 32 -Powershell
    # @python -c "import secrets; print(secrets.token_hex(32))" -Python
    SECRET_KEY :str
    ALGORITHM :str
    ACCESS_TOKEN_EXPIRE_MINUTES : int
    ORACLE_POOL_SIZE :int
    ORACLE_MAX_OVERFLOW :int
    
    model_config = SettingsConfigDict(env_file="app/.env")
  
@lru_cache   
def get_settings():
    return Settings()
from pathlib import Path
from pydantic_settings import BaseSettings


BASE_DIR = Path(__file__).parent.parent

class Config(BaseSettings):
    host: str
    port: int

    model_config = {
        "env_file": "conf/.env",
        "env_file_encoding": "utf-8"
    }

CONFIG = Config()

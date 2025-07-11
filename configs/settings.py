from pydantic import SecretStr, Field
from pydantic_settings import BaseSettings
from pathlib import Path

def find_project_root():
    current = Path(__file__).parent
    while not (current / ".git").exists() and not (current / "pyproject.toml").exists():
        if current.parent == current:
            return Path.cwd()
        current = current.parent
    return current

PROJECT_ROOT = find_project_root()

class UserData(BaseSettings):
    server : str = Field(..., alias="SMTP_SERVER")
    port : str = Field(..., alias="SMTP_PORT")
    username : str = Field(..., alias="SMTP_USERNAME")
    password : str = Field(..., alias="SMTP_PASSWORD")

    class Config:
        env_file = PROJECT_ROOT / ".env.local" if Path(".env.local").exists() else None
        env_prefix = "SMTP_"



user_data = UserData()
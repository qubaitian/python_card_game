from pydantic import BaseModel

class Config(BaseModel):
    window_width: int = 1280
    window_height: int = 720
    server: str = "localhost:8080"
    private_key: str = ""
    assets_path: str = "assets"

config = Config()
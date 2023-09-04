import os
from dataclasses import dataclass, field
from enum import Enum
from typing import List


@dataclass
class Config:
    """
    Configuration class.
    """
    basic_auth_enable: bool = os.environ.get("BASIC_AUTH_ENABLE", "false")
    basic_auth_username: str = os.environ.get("BASIC_AUTH_USERNAME", "atlaslabs")
    basic_auth_password: str = os.environ.get("BASIC_AUTH_PASSWORD", "goodatlas")

    root_path: str = str(os.environ.get("ROOT_PATH", ""))
    server_path: str = str(os.environ.get("SERVER_PATH", ""))
    openapi_url: str = str(os.environ.get("OPENAPI_URL", "/openapi.json"))
    swagger_url: str = str(os.environ.get("SWAGGER_URL", "/documentation"))


config = Config()

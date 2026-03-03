from pydantic import BaseModel, ConfigDict


class User(BaseModel):
    username: str
    username_display: str
    full_name: str
    type: int
    avatar_url: str | None = None

    model_config = ConfigDict(from_attributes=True)

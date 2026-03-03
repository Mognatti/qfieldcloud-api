from pydantic import BaseModel, Field


class CreateUserRequest(BaseModel):
    username: str = Field(..., title="Username")
    email: str = Field(..., title="Email")


class LoginRequest(BaseModel):
    username: str = Field(..., title="Username")
    password: str = Field(..., title="Password")

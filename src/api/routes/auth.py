from fastapi import APIRouter


class AuthRouter:
    router = APIRouter(prefix="/auth", tags=["Auth"])

from fastapi import APIRouter


class HealthRouter:
    router = APIRouter(prefix="/health", tags=["Health"])

    @router.get("/")
    @staticmethod
    def health():
        return {"status": "ok"}

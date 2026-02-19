from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.config.dependency import Dependency

from src.api.routes.health import HealthRouter


def create_app() -> FastAPI:
    Dependency()

    app = FastAPI(
        title="QFieldCloud - API",
        description="API para fazer chamadas intermediárias ao projeto gerenciado pelo QFieldCloud",
    )

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    routers = [HealthRouter]

    for router in routers:
        app.include_router(router.router)

    return app

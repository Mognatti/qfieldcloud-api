from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.config.dependency import Container

from src.api.routes.health import HealthRouter
from src.api.routes.project import ProjectRouter
from src.api.routes.auth import AuthRouter
from src.api.routes.user import UserRouter


def create_app() -> FastAPI:
    Container()

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

    routers = [HealthRouter, ProjectRouter, AuthRouter, UserRouter]

    for router in routers:
        app.include_router(router.router)

    return app

from fastapi import APIRouter, Depends
from dependency_injector.wiring import Provide, inject
from typing import Annotated

from src.config.dependency import Container
from src.domain.services.qfieldcloud import QFieldCloudService
from src.api.schemas.request import ListPaginatedItemsRequest
from src.api.schemas.request.user import CreateUserRequest, LoginRequest
from src.api.meta.user import list_users_meta

class UserRouter:
    router = APIRouter(prefix="/user", tags=["User"])

    @staticmethod
    @router.get("/", **list_users_meta())
    @inject
    def list_users(
        service: Annotated[
            QFieldCloudService, Depends(Provide[Container.qfieldcloud_service])
        ],
    payload: Annotated[ListPaginatedItemsRequest, Depends()],
    ):
        return service.list_users(payload)

    @staticmethod
    @router.post("/")
    @inject
    def create_user(
        payload: CreateUserRequest,
        service: Annotated[
            QFieldCloudService, Depends(Provide[Container.qfieldcloud_service])
        ],
    ):
        return service.create_user(payload)

    @staticmethod
    @router.post("/login")
    @inject
    def login_user(
        payload: LoginRequest,
        service: Annotated[
            QFieldCloudService, Depends(Provide[Container.qfieldcloud_service])
        ],
    ):
        return service.login(payload)

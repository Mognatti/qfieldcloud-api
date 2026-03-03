from typing import Annotated
from fastapi import APIRouter, Depends
from dependency_injector.wiring import Provide, inject

from src.config.dependency import Container
from src.domain.services.qfieldcloud import QFieldCloudService
from src.api.schemas.request.project import CreateProjectRequest
from src.api.meta.project import create_project_meta


class ProjectRouter:
    router = APIRouter(prefix="/project", tags=["Project"])

    @staticmethod
    @router.get("/")
    @inject
    def list_projects(
        service: Annotated[
            QFieldCloudService, Depends(Provide[Container.qfieldcloud_service])
        ],
    ):
        return service.list_projects()

    @staticmethod
    @router.get("/{project_id}/collaborators/")
    @inject
    def get_project_collaborators(
        project_id: str,
        service: Annotated[
            QFieldCloudService, Depends(Provide[Container.qfieldcloud_service])
        ],
    ):
        return service.get_project_collaborators(project_id=project_id)

    @staticmethod
    @router.post("/", **create_project_meta())
    @inject
    def create_project(
        payload: CreateProjectRequest,
        service: Annotated[
            QFieldCloudService, Depends(Provide[Container.qfieldcloud_service])
        ],
    ):
        return service.create_project(payload)

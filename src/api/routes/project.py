import os
import tempfile
import shutil
from typing import Annotated
from fastapi import APIRouter, Depends, File, UploadFile
from dependency_injector.wiring import Provide, inject

from src.config.dependency import Container
from src.domain.services.qfieldcloud import QFieldCloudService
from src.api.schemas.request.project import (
    CreateProjectRequest,
    AssociateCollaboratorRequest,
)
from src.api.schemas.request import ListPaginatedItemsRequest
from src.api.meta.project import (
    create_project_meta,
    list_projects_meta,
    associate_collaborator_meta,
)


class ProjectRouter:
    router = APIRouter(prefix="/project", tags=["Project"])

    @staticmethod
    @router.get("/", **list_projects_meta())
    @inject
    def list_projects(
        params: Annotated[ListPaginatedItemsRequest, Depends()],
        service: Annotated[
            QFieldCloudService, Depends(Provide[Container.qfieldcloud_service])
        ],
    ):
        return service.list_projects(params)

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
    @router.post("/{project_id}/collaborators/", **associate_collaborator_meta())
    @inject
    def add_project_collaborator(
        payload: AssociateCollaboratorRequest,
        project_id: str,
        service: Annotated[
            QFieldCloudService, Depends(Provide[Container.qfieldcloud_service])
        ],
    ):
        return service.add_project_collaborator(project_id=project_id, payload=payload)

    @staticmethod
    @router.get("/aux/project-roles")
    @inject
    def get_project_roles(
        service: Annotated[
            QFieldCloudService, Depends(Provide[Container.qfieldcloud_service])
        ],
    ):
        return service.get_project_roles()

    @staticmethod
    @router.post("/{project_id}/files")
    @inject
    def upload_files(
        project_id: str,
        files: list[UploadFile] = File(...),
        service: Annotated[
            QFieldCloudService, Depends(Provide[Container.qfieldcloud_service])
        ] = None,
    ):
        with tempfile.TemporaryDirectory() as tmp_dir:
            for file in files:
                file_path = os.path.join(tmp_dir, file.filename)
                with open(file_path, "wb") as f:
                    shutil.copyfileobj(file.file, f)

            result = service.upload_project_files(
                project_id=project_id,
                project_path=tmp_dir,
            )
        return result

    @staticmethod
    @router.post("/{project_id}/repackage")
    @inject
    def repackage(
        project_id: str,
        service: Annotated[
            QFieldCloudService, Depends(Provide[Container.qfieldcloud_service])
        ],
    ):
        return service.trigger_repackaging(project_id=project_id)

    @staticmethod
    @router.get("/jobs/{job_id}")
    @inject
    def job_status(
        job_id: str,
        service: Annotated[
            QFieldCloudService, Depends(Provide[Container.qfieldcloud_service])
        ],
    ):
        return service.get_job_status(job_id=job_id)

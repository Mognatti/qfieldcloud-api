import os
from pathlib import Path
from qfieldcloud_sdk.sdk import (
    Client,
    ProjectCollaboratorRole,
    FileTransferType,
    JobTypes,
)
from src.config import settings

from src.api.schemas.request.user import CreateUserRequest, LoginRequest
from src.api.schemas.request import ListPaginatedItemsRequest
from src.api.schemas.request.project import (
    CreateProjectRequest,
    AssociateCollaboratorRequest,
)

from src.api.schemas.response.user import User
from src.api.schemas.response.project import Project
from src.api.schemas.response import ListPaginatedItems, PageMetaDto


class QFieldCloudService:
    def __init__(self):
        self.url = settings.QFIELDCLOUD_URL
        self.token = settings.QFIELDCLOUD_TOKEN
        self._client = Client(url=self.url, token=self.token, verify_ssl=False)
        self._client.verify_ssl = False

    #####################
    ##### PROJECTS ######
    #####################

    def list_projects(self, params: ListPaginatedItemsRequest):

        response = self._client.session.get(
            f"{self.url}projects/",
            headers={"Authorization": f"Token {self.token}"},
            params={"limit": params.limit, "offset": params.offset},
            verify=False,
        )

        result = {
            "data": response.json(),
            "count": int(response.headers.get("X-Total-Count", 0)),
            "next": response.headers.get("X-Next-Page"),
            "previous": response.headers.get("X-Previous-Page"),
        }

        return ListPaginatedItems(
            data=[Project(**project) for project in result["data"]],
            meta=PageMetaDto(**result),
        )

    def get_project(self, project_id: str):
        return self._client.get_project(project_id)

    def create_project(self, payload: CreateProjectRequest):
        project = self._client.create_project(
            name=payload.name,
            description=payload.description,
            is_public=False,
        )

        if payload.admin:
            self._client.add_project_collaborator(
                project_id=project["id"],
                username=payload.admin,
                role="admin",
            )

        return project

    def get_project_collaborators(self, project_id: str):
        return self._client.get_project_collaborators(project_id=project_id)

    def add_project_collaborator(
        self, project_id: str, payload: AssociateCollaboratorRequest
    ):
        return self._client.add_project_collaborator(
            project_id=project_id, username=payload.username, role=payload.role
        )

    def upload_project_files(self, project_id: str, project_path: str):
        results = []
        for filename in os.listdir(project_path):
            local_path = Path(project_path) / filename
            if not local_path.is_file():
                continue

            with open(local_path, "rb") as f:
                response = self._client.session.post(
                    f"{self.url}files/{project_id}/{filename}/",
                    headers={"Authorization": f"Token {self.token}"},
                    files={"file": (filename, f)},
                    verify=False,
                )

            results.append(
                {
                    "filename": filename,
                    "status_code": response.status_code,
                    "response": response.text,
                }
            )

        return results

    def trigger_repackaging(self, project_id: str):
        """Dispara o processamento do projeto"""
        return self._client.job_trigger(
            project_id=project_id,
            job_type=JobTypes.PACKAGE,
        )

    def get_job_status(self, job_id: str):
        """Verifica o status do processamento"""
        return self._client.job_status(
            job_id=job_id,
        )

    def list_project_files(self, project_id: str):
        """Lista os arquivos de um projeto"""
        return self._client.list_remote_files(
            project_id=project_id,
            upload_type=FileTransferType.PROJECT,
        )

    ####################
    ###### USERS #######
    ####################

    def list_users(self, params: ListPaginatedItemsRequest) -> ListPaginatedItems[User]:

        response = self._client.session.get(
            f"{self.url}users/",
            headers={"Authorization": f"Token {self.token}"},
            params={"limit": params.limit, "offset": params.offset},
            verify=False,
        )

        result = {
            "data": response.json(),
            "count": int(response.headers.get("X-Total-Count", 0)),
            "next": response.headers.get("X-Next-Page"),
            "previous": response.headers.get("X-Previous-Page"),
        }

        return ListPaginatedItems(
            data=[User(**user) for user in result["data"]], meta=PageMetaDto(**result)
        )

    def create_user(self, payload: CreateUserRequest):
        url = f"{self.url}admin/users/"
        body = {
            "username": payload.username,
            "email": payload.email,
        }
        headers = {"Authorization": f"Token {self.token}"}
        response = self._client.session.post(
            url, headers=headers, json=body, verify=False
        )
        return response.json()

    def login(self, payload: LoginRequest):
        url = f"{self.url}auth/token/"
        body = {
            "username": payload.username,
            "password": payload.password,
        }
        response = self._client.session.post(url, json=body, verify=False)
        return response.json()

    ####################
    ####### AUX ########
    ####################

    def get_project_roles(self):
        return [role.value for role in ProjectCollaboratorRole]

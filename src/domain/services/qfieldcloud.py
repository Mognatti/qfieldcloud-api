from qfieldcloud_sdk.sdk import Client, FileTransferType
from src.config import settings

from src.api.schemas.request.project import CreateProjectRequest

from src.api.schemas.request.user import CreateUserRequest, LoginRequest
from src.api.schemas.response.user import User
from src.api.schemas.response import ListPaginatedItems, PageMetaDto

from src.api.schemas.request import ListPaginatedItemsRequest


class QFieldCloudService:
    def __init__(self):
        self.url = settings.QFIELDCLOUD_URL
        self.token = settings.QFIELDCLOUD_TOKEN
        self._client = Client(url=self.url, token=self.token, verify_ssl=False)

    #####################
    ##### PROJECTS ######
    #####################

    def list_projects(self):
        return self._client.list_projects()

    def get_project(self, project_id: str):
        return self._client.get_project(project_id)

    def create_project(self, payload: CreateProjectRequest):
        project = self._client.create_project(
            name=payload.name,
            description=payload.description,
            is_public=False,
        )

        self._client.add_project_collaborator(
            project_id=project["id"],
            username=payload.admin,
            role="admin",
        )
        return project

    def get_project_collaborators(self, project_id: str):
        return self._client.get_project_collaborators(project_id=project_id)

    def upload_files(self, project_id: str, local_directory: str):
        return self._client.upload_files(
            project_id=project_id,
            upload_type=FileTransferType.PROJECT,
            local_directory=local_directory,
        )

    def add_project_collaborator(self, project_id: str, username: str):
        return self._client.add_project_collaborator(
            project_id=project_id, username=username
        )

    ####################
    ###### USERS #######
    ####################

    def list_users(
        self, payload: ListPaginatedItemsRequest
    ) -> ListPaginatedItems[User]:

        response = self._client.session.get(
            f"{self.url}users/",
            headers={"Authorization": f"Token {self.token}"},
            params={"limit": payload.limit, "offset": payload.offset},
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

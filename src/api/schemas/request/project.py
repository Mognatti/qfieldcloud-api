from pydantic import BaseModel, Field
from qfieldcloud_sdk.sdk import ProjectCollaboratorRole


class CreateProjectRequest(BaseModel):
    name: str = Field(..., title="Nome do projeto")
    admin: str | None = Field(None, title="Usuário dono do projeto")
    description: str = Field(..., title="Descrição do projeto")


class AssociateCollaboratorRequest(BaseModel):
    username: str = Field(..., title="Usuário colaborador")
    role: ProjectCollaboratorRole = Field(
        ..., title="Função do colaborador dentro do projeto"
    )

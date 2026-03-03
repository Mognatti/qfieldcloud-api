from pydantic import BaseModel, Field


class CreateProjectRequest(BaseModel):
    name: str = Field(..., title="Nome do projeto")
    admin: str = Field(..., title="Usuário dono do projeto")
    description: str = Field(..., title="Descrição do projeto")
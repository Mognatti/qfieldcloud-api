from starlette import status
from src.api.schemas.response.project import Project
from src.api.schemas.response import ListPaginatedItems
from qfieldcloud_sdk.sdk import CollaboratorModel


def create_project_meta():
    return {
        "status_code": status.HTTP_201_CREATED,
        "response_model": Project,
        "summary": "Cria um novo projeto",
    }


def list_projects_meta():
    return {
        "status_code": status.HTTP_200_OK,
        "response_model": ListPaginatedItems[Project],
        "summary": "Retorna lista de projetos",
    }


def associate_collaborator_meta():
    return {
        "status_code": status.HTTP_200_OK,
        "response_model": CollaboratorModel,
        "summary": "Associa um colaborador ao projeto",
    }

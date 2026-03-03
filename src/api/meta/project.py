from starlette import status

from src.api.schemas.response.project import Project

def create_project_meta():
    return {
        'status_code': status.HTTP_201_CREATED,
        # 'response_model': Project,
        'summary': 'Cria um novo projeto',
    }
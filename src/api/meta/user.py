from starlette import status

from src.api.schemas.response.user import User
from src.api.schemas.response import ListPaginatedItems

def list_users_meta():
    return {
        'status_code': status.HTTP_200_OK,
        'response_model': ListPaginatedItems[User],
        'summary': 'Retorna lista de usuários',
    }
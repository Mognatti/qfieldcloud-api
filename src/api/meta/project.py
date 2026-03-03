from starlette import status



def create_project_meta():
    return {
        "status_code": status.HTTP_201_CREATED,
        # 'response_model': Project,
        "summary": "Cria um novo projeto",
    }

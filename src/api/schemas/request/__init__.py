from pydantic import BaseModel, Field


class ListPaginatedItemsRequest(BaseModel):
    limit: int | None = Field(
        default=10, ge=1, description="Número de itens por página"
    )
    offset: int | None = Field(
        default=0, ge=0, description="Quantidade de itens a serem pulados"
    )

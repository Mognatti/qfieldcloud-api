from pydantic import BaseModel, Field, ConfigDict
from typing import Generic, TypeVar

T = TypeVar("T")


class PageMetaDto(BaseModel):
    count: int
    next: str | None = None
    previous: str | None = None


class ListPaginatedItems(BaseModel, Generic[T]):
    data: list[T] = Field(..., description="Lista de itens paginados")
    meta: PageMetaDto

    model_config = ConfigDict(from_attributes=True, arbitrary_types_allowed=True)

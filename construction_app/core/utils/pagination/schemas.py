from pydantic import Field, AnyHttpUrl
from pydantic.generics import GenericModel
from pydantic import BaseModel
from typing import Optional, Generic, TypeVar, List

M = TypeVar('M')

class PaginatedResponse(BaseModel, Generic[M]):
    count: int = Field(description='Number of items returned in the response')
    items: List[M] = Field(description='List of items returned in the response following give criteris')
    next_page: Optional[AnyHttpUrl] = Field(None, description='url of the next page if it exists')
    pervious_page: Optional[AnyHttpUrl] = Field(None, description='url of the previous page if it exists')
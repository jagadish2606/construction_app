from typing import Any, Optional
from sqlmodel import SQLModel


class ResponseModel(SQLModel):
    """standard response model for all uppaginated apis
    
    Args:
        SQLModel (_type_): _description_
    """
    data: Optional[Any] = []
    status: int = 200
    message: Optional[str] = 'ok'
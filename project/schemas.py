from typing import Optional

from pydantic import BaseModel


class CategorySchema(BaseModel):
    id: Optional[int]
    name: str
    url: str
    website: str

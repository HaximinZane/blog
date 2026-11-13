from pydantic import BaseModel,Field
from enum import Enum

class Status(str,Enum):
    DRAFT = "draft"
    PUBLISHED = "published"
    ARCHIVED = "archived"


class PostCreate(BaseModel):
    author_id : int
    title : str = Field(...,max_length=100)
    summary : str | None = None
    content : str = ""
    status : Status = Status.DRAFT
    tags : list[str] = Field([],max_length=10)
    
from pydantic import BaseModel, HttpUrl
from datetime import datetime

class ShortenRequest(BaseModel):
    url: HttpUrl

class URLResponse(BaseModel):
    id: int
    original_url: str
    short_code: str
    click_count: int
    created_at: datetime

    class Config:
        from_attributes = True
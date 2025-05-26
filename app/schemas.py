from pydantic import BaseModel
from typing import Dict, Optional


class LoadTestRequest(BaseModel):
    url: str
    method: str
    params: Optional[Dict[str, str]]
    headers: Optional[Dict[str, str]]
    body: Optional[str]
    cookies: Optional[Dict[str, str]]
    total_requests: int
    threads: int

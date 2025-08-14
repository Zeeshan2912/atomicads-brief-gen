from pydantic import BaseModel, Field, HttpUrl
from typing import List, Optional, Dict, Any
from datetime import datetime

class SourceSummary(BaseModel):
    title: str
    url: Optional[HttpUrl]
    snippet: str
    rank: Optional[int] = None

class FinalBrief(BaseModel):
    topic: str
    depth: int = Field(..., ge=0, le=5)
    summary: str
    key_findings: List[str]
    sources: List[SourceSummary]
    plan: List[str]
    metadata: Dict[str, Any]
    generated_at: datetime

from typing import List, Optional
from pydantic import BaseModel, Field


class ResearchSource(BaseModel):
    """Represents one collected research source."""

    title: str
    url: str
    content: str
    score: float = 0.0


class ResearchResult(BaseModel):
    """Stores the output of the Research Agent."""

    topic: str
    summary: str
    sources: List[ResearchSource] = Field(default_factory=list)


class ResearchState(BaseModel):
    """Shared information for the research workflow."""

    topic: str
    plan: str = ""
    research: Optional[ResearchResult] = None
    analysis: str = ""
    report: str = ""
    fact_check: str = ""
    review: str = ""
    status: str = "pending"
    revision_count: int = 0
  
